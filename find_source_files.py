#!/usr/bin/python3
import sys
import tarfile
import tempfile
import zipfile
import os
import shutil
import itertools
import filehash
from pathlib import Path
# Go through none directory

DATASET_DIR = '/Users/logancheng/Downloads/RESULT'#'/data2/pypi'

def iterate(directory):
    
    for subdir, dirs, files in os.walk(directory):
        destination = os.path.join(DATASET_DIR, Path(subdir).parts[-1])
        for file in files:
            if file.endswith('.tar.gz'):
                tar_func(file, subdir, destination)
            elif file.endswith('.egg'):
                egg_func(file, subdir, destination)
            elif file.endswith('.whl'):
                whl_func(file, subdir, destination)
            elif file.endswith('.zip'):
                unzip(file, subdir, destination)
            else:
                print(f'[UNCATEGORIZED] {file}')

def is_extractable(filename: str) -> bool:
        if not filename.endswith('.py'):
            return False
        if filename.endswith('__init__.py'):
            return False
        if filename.endswith('/setup.py'):
            return False
        return True

def hash_file(filepath):
    sha512hasher = filehash.FileHash('sha512')
    return sha512hasher.hash_file(filepath)

def flatten(destination):
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk(destination), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
        shutil.move(filename, destination)
    
    for name in os.listdir(destination):
        path = Path(destination).joinpath(Path(name)).resolve()
        if os.path.isdir(path):
            shutil.rmtree(path)

# Does egg and whl files
def unzip(filename, file_directory, destination):
    with tempfile.TemporaryDirectory() as tempdir:
        path_to_file = os.path.join(file_directory, filename)
        with zipfile.ZipFile(path_to_file, 'r') as file:
            file.extractall(tempdir)
        
        extractable_files = []
        for subdir, _, files in os.walk(tempdir):
            extractable_files.extend(os.path.join(subdir, file) for file in files if is_extractable(file))
    
        for index, file in enumerate(extractable_files):
            filename = Path(file).name
            new_dir = Path(destination).with_name(hash_file(file))
            os.makedirs(new_dir, exist_ok=True)
            new_location = new_dir.joinpath(filename)
            shutil.move(file, new_location)
            flatten(new_dir)


# extracts egg files
def egg_func(filename, cwd, destination):
    unzip(filename, cwd, destination)

# extracts whl files
def whl_func(filename, cwd, destination):
    unzip(filename, cwd, destination)

# extracts tar files
def tar_func(filename, cwd, destination):
    with tempfile.TemporaryDirectory() as tempdir:
        filepath = os.path.join(cwd, filename)
        tar = tarfile.open(filepath)
        tar.extractall(tempdir)
        extractable_files = []
        for subdir, _, files in os.walk(tempdir):
            extractable_files.extend(os.path.join(subdir, file) for file in files if is_extractable(file))
        for index, file in enumerate(extractable_files):
            filename = Path(file).name
            new_dir = Path(destination).with_name(hash_file(file))
            os.makedirs(new_dir, exist_ok=True)
            new_location = new_dir.joinpath(filename)
            shutil.move(file, new_location)
            flatten(new_dir)
    # with tarfile.open(filepath) as file:
    #     extractable_members = (member for member in file.getmembers() if member.isfile() and is_extractable(member.name))
    #     for index, member in enumerate(extractable_members):
    #         member_destination = Path(destination).with_name(hash_file())
    #         os.makedirs(member_destination, exist_ok=True)
    #         file.extract(member, member_destination)
    #         flatten(member_destination)

if __name__ == '__main__':
    directory = os.getcwd()
    scraped_file_directory = os.path.join(directory, "None")
    iterate(scraped_file_directory)
