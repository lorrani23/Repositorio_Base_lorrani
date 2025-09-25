import requests


response = requests.get("https://www.instagram.com/")


if 200 <= response.status_code <= 299:
    print("site ok ")

elif 400 <= response.status_code <=499:
    print("site nao encontrado")
else:
    print("nao encontrado")
