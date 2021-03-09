# Guild Wars 2 API Python Wrapper

|Build Status|

## Installation
- Pre-requisites: Python >= 3.6
- Install the [package](https://pypi.org/project/gw2apy/) from PyPi directly:
```bash
pip install gw2apy
```

## Quickstart
- Create a client:
```python
from gw2apy.client import Client

client = Client()
```
You can specify an API key to access authenticated endpoints, such as bank content or wallet:
```python
client = Client(api_key="YOUR_API_KEY")
```

- Create an endpoint, e.g. Items: 
```python
from gw2apy.endpoints import Items

items_endpoint = Items(client=client)

items_endpoint.id(id=28445)
```

- Request data from the endpoint:
```python
# Returns the list of ids for all available items.
items_ids = items_endpoint.endpoint()

# Return the item associated to an id.
item = items_endpoint.id(id=28445)

# Return a list of item given a list of ids.
items = items_endpoint.ids(ids=[28445, 12452])

# Return a list of all the items.
all_items = items_endpoint.all()
```

