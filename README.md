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

usage: bulkydownload.py [-h] [-u URL]

optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url URL  for selecting the bulk audio web url
```
### Example

`python bulkydownload.py -u <bulk-audio-url>`