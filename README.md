# diagnosis-disease-based-symptoms
Simple program that demonstrates how it is possible based on symptoms, define which disease. The goal is to show how to get a simple diagnosis, integrating Python with Prolog to create a mini expert system with Symbolic Artificial Intelligence concept.

### Tech

Dillinger uses a number of open source projects to work properly:

* [Python 3.6.4] - For the backend
* [Flask Framework] - Python microframework
* [prolog-swi] - Free Prolog environment

### Docker
Dillinger is very easy to install and deploy in a Docker container.

In order to execute the application, it is necessary to perform the build of the docker compose, done that, the application can already be executed with the compose up.

```sh
cd diagnosis-disease-based-symptoms
docker-compose build
```

Run application in production environment

```sh
cd diagnosis-disease-based-symptoms
docker-compose up
```

### Manually
To deploy the application manually, simply install the requirements

```sh
cd diagnosis-disease-based-symptoms
pip install -r requirements.txt
```

Run application in production environment

```sh
cd diagnosis-disease-based-symptoms
cd app
python -m main
```
