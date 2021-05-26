FROM python:3.8-slim-buster

WORKDIR /home/action

COPY requirements.txt /home/action
COPY run.py /home/action
COPY entrypoint.sh /home/action

RUN ["chmod", "+x", "/entrypoint.sh"]

RUN apt update && apt upgrade
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt


ENTRYPOINT ["/entrypoint.sh"]