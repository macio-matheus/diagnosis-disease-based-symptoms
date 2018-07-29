FROM python:3.6.4

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y swi-prolog

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080