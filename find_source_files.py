#!/usr/bin/python3
from fileinput import filename
import sys
import tarfile
import tempfile
from typing import Callable
import zipfile
import os
import shutil
import itertools
import filehash
from pathlib import Path
# Go through none directory

DATASET_DIR = '/data2/pypi'

def iterate(directory: str) -> None:
    for subdir, dirs, files in os.walk(directory):
        destination = os.path.join(DATASET_DIR, Path(subdir).parts[-1])
        for file in files:
            if file.endswith('.tar.gz'):
                extract(file, subdir, destination, tar_extractor_strategy)
            elif file.endswith('.egg'):
                extract(file, subdir, destination, unzip_strategy)
            elif file.endswith('.whl'):
                extract(file, subdir, destination, unzip_strategy)
            elif file.endswith('.zip'):
                extract(file, subdir, destination, unzip_strategy)
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

def hash_file(filepath: str) -> str:
    sha512hasher = filehash.FileHash('sha512')
    return sha512hasher.hash_file(filepath)

def flatten(destination: str) -> None:
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
def unzip_strategy(filepath: str, destination: str) -> None:
    with zipfile.ZipFile(filepath, 'r') as file:
            file.extractall(destination)

# extracts tar files
def tar_extractor_strategy(filepath: str, destination: str) -> None:
    tar = tarfile.open(filepath)
    tar.extractall(destination)

def extract(filename: str, file_directory: str, destination: str, extractor_strategy: Callable[[str, str], None]) -> None:
    with tempfile.TemporaryDirectory() as tempdir:
        filepath = os.path.join(file_directory, filename)
        extractor_strategy(filepath, tempdir)
        for subdir, _, files in os.walk(tempdir):
            for file in map(lambda name: os.path.join(subdir, name), files):
                if not is_extractable(file):
                    continue
                filename = Path(file).name
                new_dir = Path(destination).with_name(hash_file(file))
                os.makedirs(new_dir, exist_ok=True)
                new_location = new_dir.joinpath(filename)
                shutil.move(file, new_location)
                flatten(new_dir)

if __name__ == '__main__':
    directory = os.getcwd()
    scraped_file_directory = os.path.join(directory, "None")
    iterate(scraped_file_directory)
