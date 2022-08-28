import requests

def getdog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")

    print("response.status_code returned ", response.status_code)
    r = response.json()

    return r["message"] 

# getdog()
