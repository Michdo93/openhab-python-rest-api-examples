import requests
from requests.auth import HTTPBasicAuth

base_url = "http://<ip_address>:8080/rest"
session = requests.Session()
session.auth = ('<username>', '<password>')
headers = {"Content-type": "application/json"}
session.headers.update(headers)

items = ["testColor", "testContact", "testDateTime", "testDimmer", "testImage", "testLocation", "testNumber", "testPlayer", "testRollershutter", "testString", "testSwitch"]

try:
    login_response = session.get(base_url, headers=headers, timeout=8)
    login_response.raise_for_status()

    if login_response.ok or login_response.status_code == 200:
        for item in items:
            url = base_url + "/items/" + item + "/state"
            response = session.get(url, headers=headers, timeout=8)
            response.raise_for_status()

            if response.ok or response.status_code == 200:
                print(response.text)
    else:
        print(login_response.text)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
