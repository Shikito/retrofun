FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV SERVICE_NAME py11

# Language Setup
RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

# X11 install
RUN apt-get update -y\
 && apt-get install x11-apps -y
ENV DISPLAY host.docker.internal:0.0

# Python install
WORKDIR /${SERVICE_NAME}
ADD docker/${SERVICE_NAME}/etc/requirements.txt /${SERVICE_NAME}/
RUN apt-get -y update && \
    apt-get -y install \
    apt-utils \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Apt Packege install
RUN apt-get update \
    && apt-get install -y cron