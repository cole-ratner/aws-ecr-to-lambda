FROM python:3.8-slim-buster

COPY requirements.txt .

RUN apt update && apt upgrade
RUN pip install -r requirements.txt

ADD run.py /run.py
ADD entrypoint.sh /entrypoint.sh

RUN ["chmod", "+x", "/entrypoint.sh"]

ENTRYPOINT ["/entrypoint.sh"]