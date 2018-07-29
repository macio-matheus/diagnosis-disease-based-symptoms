# diagnosis-disease-based-symptoms
Simple API to demonstrate a Knowledge Based System (KBS). The KBS concept can be defined as methods that search in a space of possible solutions, using heuristics to make this search more efficient.


### KBS Architecture 

![KBS architecture](https://raw.githubusercontent.com/macio-matheus/diagnosis-disease-based-symptoms/master/KBS-architecture.jpeg)

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

### Symptoms
Available Symptoms
OBS: Select 5 symptoms per request, as in the example

```sh
{
    "symptoms": [
        "dor_cabeca",
        "dor_facial",
        "dor_garganta",
        "febre",
        "inchaco_tempora", 
        "dor_atras_olhos",
        "perda_paladar",
        "tontura",
        "bolhas_vermelhas",
        "coceira",
        "dor_barriga"
    ]
}
```

output

```sh
{
  "diagnosis": "caxumba"
}
```

### Basic example
Example of request that returns the diagnosis of caxumba

```sh
import requests

url = "http://192.168.99.100:8080/diagnosis"

payload = "{\n    \"symptoms\": [\n        \"febre\",\n        \"bolhas_vermelhas\",\n        \"coceira\",\n        " \
          "\"dor_cabeca\",\n        \"dor_barriga\"\n    ]\n} "
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```

output

```sh
{
  "diagnosis": "caxumba"
}
```
