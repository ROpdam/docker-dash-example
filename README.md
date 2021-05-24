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
To run the image locally, cd into the project folder and build the container:
```
docker build -t docker-dash .
```
And run the container
```
docker run -p 8050:8050 docker-dash
```
This way the image is created using the Dockerfile, instead of the Dockerfile.prod. You can find to the app on your local machine http://0.0.0.0:8050/
