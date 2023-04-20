import requests
from requests.auth import HTTPBasicAuth
import json

base_url = "http://<ip_address>:8080/rest"
auth = HTTPBasicAuth('<username>', '<password>')
headers = {"Content-type": "application/json"}

url = base_url + "/items"

try:
    response = requests.get(url, auth=auth, headers=headers, timeout=8)
    response.raise_for_status()

    if response.ok or response.status_code == 200:
        items = json.loads(response.text) # list of dicts

        for item in items:
            item_type = item.get("type")
            item_name = item.get("name")
            item_state = item.get("state")

            print("Received item type " + item_type + " with name " + item_name + " and state " + item_state)
    else:
        print(response.text)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
