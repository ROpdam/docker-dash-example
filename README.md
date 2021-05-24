# Docker Dash Example
A simple design for a plotly-dash app with sklearn running within a docker container deployed to [Heroku](https://docker-dash.herokuapp.com) using CI/CD. [![Continuous Integration and Delivery](https://github.com/ROpdam/docker-dash-example/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/ROpdam/docker-dash-example/actions/workflows/main.yml)
### Using [pre-commit-hooks](https://pre-commit.com/)
- flake8 
- black

### Structure
```
├── project
│   ├── app
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── functions.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── .github
│   └── workflows
│        └── main.yml
│
├── release.sh
├── setup.cfg
├── .pre-commit-config.yaml
├── .gitignore
│
└── README.md
```

### Run locally
To run the image locally change the last line in the Dockerfile from
```
CMD gunicorn --bind 0.0.0.0:$PORT --chdir app/ app:server
```
to
```
CMD gunicorn --bind 0.0.0.0:8050 --chdir app/ app:server
```
Then build the image
```
docker build -t docker-dash .
```
And run the container
```
docker run -p 8050:8050 docker-dash
```
You can find to the app on your local machine http://0.0.0.0:8050/
