FROM ubuntu:18.04
WORKDIR /soup
RUN pip install requirements.txt
COPY . ./
CMD python bulkydownload.py -h
