FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app/
RUN apt-get update && apt-get install -y python3.9 python3-pip
COPY ./app .
RUN pip3 install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8888 app:app