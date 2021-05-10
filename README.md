# Docker Dash Example
A simple design for a plotly-dash app with sklearn running within a docker container deployed to [Heroku](https://docker-dash.herokuapp.com) using CI/CD.
### Using [pre-commit-hooks](https://pre-commit.com/)
- flake8 
- black

### Structure
```
├── project
│   ├── app
│   │   ├── functions.py
│   │   └── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── setup.cfg
├── .pre-commit-config.yaml
├── .gitignore
│
└── README.md
```

### Run locally
To run the image locally change
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