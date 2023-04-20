# openHAB Python REST API examples
Examples how to use the openHAB REST API with Python. Whether via the cloud or locally.

For testing you can install the [openhab_static_examples](https://github.com/Michdo93/openhab_static_examples/).

## How to use

A good instruction how to work with the openHAB REST API can be found [here](https://github.com/Michdo93/openhab_postman_templates).

### Accessing a local openHAB instance

Please replace `<ip_address>` with the ip address of you local openHAB instance. Also you have to replace `<username>` and `<password>` with the username and password of your local openHAB instance. Depending on the configuration, it may even be possible to omit authentication with user name and password when accessing a locally installed instance. In this case, you can remove the header altogether by inserting null.

### Accessing the openHAB Cloud

You have to replace `<email_address>` and `<password>` with the email address and password of your openHAB Cloud account.
