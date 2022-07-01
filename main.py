#!/usr/bin/python3
import argparse
import feedparser
import requests
import os
import sys
from tqdm import tqdm
from ratelimit import limits, sleep_and_retry
from datetime import timedelta


@sleep_and_retry
@limits(calls=100, period=timedelta(seconds=60).total_seconds())
def get_latest_release(project, release):
    url = f"https://pypi.org/pypi/{project}/{release}/json"
    r = requests.get(url)
    try:
        release_entry = r.json()["releases"][release]
        if not release_entry:
            return None
        download = release_entry[-1]["url"]
        return download
    except KeyError as err:
        print(f'KeyError in get_latest_release({project}, {release}): {err}', file=sys.stderr)
        return None

def parse_feed(url):
    import ssl
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    feed = feedparser.parse(url)
    downloads = []
    print(f"Parsing {len(feed.entries)} entries")
    for entry in tqdm(feed.entries):
        base_link = entry.link
        name = base_link.split('/')[-3]
        release = base_link.split('/')[-2]
        download = get_latest_release(name, release)
        if download is not None:
            downloads.append(download)
    return downloads


def download_files(downloads, out_dir):
    print(f"Downloading {len(downloads)} files...")
    for download in tqdm(downloads):
        filename = download.split("/")[-1]
        hash_val = download.split("/")[-2]
        new_dir = f"{out_dir}/{hash_val}"
        os.makedirs(new_dir, exist_ok=True)
        out_file = f"{new_dir}/{filename}"
        with open(out_file, "wb") as f:
            r = requests.get(download, stream=True)
            if r.status_code == 200:
                f.write(r.raw.read())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir")
    args = parser.parse_args()

    downloads = parse_feed("https://pypi.org/rss/updates.xml")
    download_files(downloads, args.out_dir)
