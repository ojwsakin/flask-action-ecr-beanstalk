FROM python:3

RUN apt update
RUN apt install -y python3-pip
WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
