import requests

base_url = "https://myopenhab.org"
session = requests.Session()
auth = ('<email_address>', '<password>')
session.auth = auth
headers = {"Content-type": "text/plain; charset=utf-8", "Accept": "text/plain"}
session.headers.update(headers)

url = base_url + "/rest/items/testDateTime"
data = "2022-08-22T21:48:10"


try:
    login_response = session.get(base_url, auth=auth, headers=headers, timeout=8)
    login_response.raise_for_status()

    if login_response.ok or login_response.status_code == 200:
        response = session.post(url, auth=auth, data=data, headers=headers, timeout=8)
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

