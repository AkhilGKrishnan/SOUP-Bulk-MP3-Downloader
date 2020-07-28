# SOUP-Bulk-File-Downloader

[![Generic badge](https://img.shields.io/badge/completed-no-<COLOR>.svg)](https://shields.io/)  [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) <br>
SOUP-Bulk-File-Downloader is a BeautifulSoup based bulk file downloader. You can download bulk files from the web by a single run.

## Requirements

* Python 3.6+
* BeautifulSOUP
* requests

## Installation

`pip install requirements.txt`

## Commands


```
python bulkydownload.py -h

usage: bulkydownload.py [-h] -u URL [-p PATH] -e EXTENSION

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     for choosing the web url for downloadind the files
  -p PATH, --path PATH  folder path for storing the downloaded files
  -e EXTENSION, --extension EXTENSION
                        for choosing the file extension
```
### Example

`python bulkydownload.py -u <bulk-audio-url> -e <file-extension>`