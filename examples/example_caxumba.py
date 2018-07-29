import requests

url = "http://192.168.99.100:8080/diagnosis"

payload = "{\n    \"symptoms\": [\n        \"dor_cabeca\",\n        \"dor_facial\",\n        \"dor_garganta\"," \
          "\n        \"febre\",\n        \"inchaco_tempora\"\n    ]\n} "
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
