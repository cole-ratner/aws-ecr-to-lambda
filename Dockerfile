FROM python:3.8-slim-buster

COPY ./requirements.txt .

RUN apt update \
  && apt upgrade \
  && apt add --no-cache --update python3 python py-pip coreutils \
  && rm -rf /var/cache/apt/* \
  && pip install awscli \
  && pip install -r requirements.txt \
  && apt --purge -v del py-pip

ADD run.py /run.py
ADD entrypoint.sh /entrypoint.sh

RUN ["chmod", "+x", "/entrypoint.sh"]

ENTRYPOINT ["/entrypoint.sh"]