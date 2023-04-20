import requests
from requests.auth import HTTPBasicAuth

base_url = "http://<ip_address>:8080/rest"
auth = HTTPBasicAuth('<username>', '<password>')
headers = {"Content-type": "application/json"}

url = base_url + "/items/testString/state"

try:
    response = requests.get(url, auth=auth, headers=headers, timeout=8)
    response.raise_for_status()

    if response.ok or response.status_code == 200:
        state = response.text
        print(state)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
