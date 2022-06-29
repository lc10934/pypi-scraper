#!/bin/bash
python3 /Users/logancheng/Downloads/pypi-scraper/main.py
python3 /Users/logancheng/Downloads/pypi-scraper/find_source_files.py
zip /Users/logancheng/Downloads/pypi-scraper/py_files.zip -r -j -q /Users/logancheng/Downloads/pypi-scraper/python_sources

rm -r /Users/logancheng/Downloads/pypi-scraper/None
rm -r /Users/logancheng/Downloads/pypi-scraper/tar_files
rm -r /Users/logancheng/Downloads/pypi-scraper/whl_files
rm -r /Users/logancheng/Downloads/pypi-scraper/egg_files
rm -r /Users/logancheng/Downloads/pypi-scraper/zip_files
rm -r /Users/logancheng/Downloads/pypi-scraper/python_sources