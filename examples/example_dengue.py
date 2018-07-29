import requests

url = "http://192.168.99.100:8080/diagnosis"

payload = "{\n    \"symptoms\": [\n        \"dor_atras_olhos\",\n        \"dor_cabeca\",\n        \"febre\"," \
          "\n        \"perda_paladar\",\n        \"tontura\"\n    ]\n} "
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
