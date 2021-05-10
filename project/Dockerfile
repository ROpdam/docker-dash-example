#From https://towardsdatascience.com/docker-for-python-dash-r-shiny-6097c8998506

FROM python:3.8.6-slim-buster

LABEL maintainer "Robin Opdam, robinopdam@hotmail.com"

# set working directory
WORKDIR /usr/src/app

COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /usr/src/app/

# EXPOSE 8050

# CMD ["python", "./app/app.py"]
CMD gunicorn --bind 0.0.0.0:$PORT --chdir app/ app:server