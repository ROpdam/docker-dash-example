# Docker Dash Example
A simple design for a plotly-dash app with sklearn running within a docker container
### Using [pre-commit-hooks](https://pre-commit.com/)
- flake8 
- black

### Setup
Build the image
```
docker-compose build
```
Run the container
```
docker-compose up
```
Go to the app on your local machine http://0.0.0.0:8050/

### Structure
```
├── app
│   ├── Dockerfile
│   ├── functions.py
│   ├── requirements.txt
│   └── app.py
│       
├── .env
├── setup.cfg
├── .pre-commit-config.yaml
├── .gitignore
│
├── docker-compose.yml
│
└── README.md
```
