import requests
import time

url = "https://copa22.medeiro.tech"

def retrieve(path : str):
    req = requests.get(url + path)
    req.raise_for_status()
    return req.json()

