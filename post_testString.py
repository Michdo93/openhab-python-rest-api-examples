import requests
from requests.auth import HTTPBasicAuth

base_url = "http://<ip_address>:8080/rest"
auth = HTTPBasicAuth('<username>', '<password>')
headers = {"Content-type": "text/plain; charset=utf-8", "Accept": "text/plain"}

url = base_url + "/items/testString"
data = "Hello World"

try:
    response = requests.post(url, auth=auth, data=data, headers=headers, timeout=8)
    response.raise_for_status()

    print(response.text)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

