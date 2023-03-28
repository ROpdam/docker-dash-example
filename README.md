- **Note:** hotfix for werkzeug issue [#1992](https://github.com/plotly/dash/issues/1992) in place
- **Note:** changed deployment from Heroku to Google Cloud Run

# Docker Dash Example
A simple design for a plotly-dash app with sklearn running within a docker container deployed to [Google Cloud Run](https://docker-dash-example.com/) using CI/CD. [![Continuous Integration and Delivery](https://github.com/ROpdam/docker-dash-example/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/ROpdam/docker-dash-example/actions/workflows/main.yml) 
 
For a deep dive on the implementation please see:
1. [Initial deployment through Heroku](https://towardsdatascience.com/deploy-containeriazed-plotly-dash-app-to-heroku-with-ci-cd-f82ca833375c). 
2. [Current deployment to GCP through Google Cloud Run](https://medium.com/towards-data-science/deploy-containerised-plotly-dash-app-with-ci-cd-p2-gcp-dfa33edc5f2f)
 
Inspired by [This TDD Course](https://testdriven.io/courses/tdd-fastapi/)
 
## Using [pre-commit-hooks](https://pre-commit.com/)
- [flake8](https://github.com/pycqa/flake8)
- [black](https://github.com/ambv/black)
- [isort](https://github.com/pycqa/isort)
- [detect-private-key](https://github.com/pre-commit/pre-commit-hooks#detect-private-key)
- [bandit](https://github.com/PyCQA/bandit)

## Repo structure
```
├── .github
│   └── workflows
│        └── main.yml
│
├── project
│   ├── app
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── functions.py
│   │   └── assets
│   ├── tests
│   │   └── test_functions.py
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   └── requirements.txt
│
├── release.sh
├── setup.cfg
├── .pre-commit-config.yaml
├── .gitignore
│
└── README.md
```

## Run locally
To run the image locally, cd into the docker-dash-example folder and:
```
docker build -t docker-dash project/.
```
And run the container
```
docker run -p 8050:8050 docker-dash
```
You can find to the app on your local machine http://localhost:8050/ (or localhost:8050). This way the image is created using the Dockerfile, instead of the Dockerfile.prod.

## Project context
This was a fun project to apply different learnings in practice, very happy to hear **your** thoughts in the repo, including feedback of course!
