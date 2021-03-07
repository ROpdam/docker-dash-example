#From https://towardsdatascience.com/docker-for-python-dash-r-shiny-6097c8998506

FROM python:3.8

LABEL maintainer "Robin Opdam, robinopdam@hotmail.com"

WORKDIR /code

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY ./ ./

EXPOSE 8050

CMD ["python", "./app.py"]