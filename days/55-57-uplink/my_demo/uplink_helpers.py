import requests
import uplink

@uplink.response_handler
def raise_for_status(response: requests.models.Response):
    response.raise_for_status()
    return response
