import requests

url = "https://witzapi.de/api/joke/?language=de"

def request():
    r = requests.get(url)
    json = r.json()
    return json[0]["text"]

print(request())
