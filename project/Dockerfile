#From https://towardsdatascience.com/docker-for-python-dash-r-shiny-6097c8998506

FROM python:3.8.6-slim-buster

LABEL maintainer "Robin Opdam, robinopdam@hotmail.com"

# set working directory
WORKDIR /usr/src/app

COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /usr/src/app/

# Run locally
CMD gunicorn --bind 0.0.0.0:8050 --chdir app/ app:server