import requests

base_url = "https://myopenhab.org"
session = requests.Session()
auth = ('<email_address>', '<password>')
session.auth = auth
headers = {"Content-type": "application/json"}
session.headers.update(headers)

url = base_url + "/rest/items/testLocation/state"


try:
    login_response = session.get(base_url, auth=auth, headers=headers, timeout=8)
    login_response.raise_for_status()

    if login_response.ok or login_response.status_code == 200:
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

