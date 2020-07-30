FROM ubuntu:18.04
RUN pip install requirements.txt
CMD python bulkydownload.py -h