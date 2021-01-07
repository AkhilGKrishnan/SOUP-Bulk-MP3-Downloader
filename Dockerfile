FROM python:3.8-alpine
WORKDIR /soup
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .