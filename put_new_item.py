import requests
from requests.auth import HTTPBasicAuth
import json

base_url = "http://<ip_address>:8080/rest"
auth = HTTPBasicAuth('<username>', '<password>')
headers = {"Content-type": "application/json", "Accept": "application/json"}

url = base_url + "/items/testItem"
data = {"type": "String", "name": "testItem", "label": "tester", "groupNames": ["testGroup"]}
data = json.dumps(data)

try:
    response = requests.put(url, auth=auth, data=data, headers=headers, timeout=8)
    response.raise_for_status()
    print(response)
    print(response.text)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
