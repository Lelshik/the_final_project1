import configuration
import requests
import data

def post_create_order(order_body) :
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=order_body)
track_number = post_create_order(data.order_body).json()["track"]

response = post_create_order(data.order_body)
print(response.status_code)
print(response.json()["track"])

def get_order_on_number():
    track = post_create_order(data.order_body).json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER + str(track))


response  = get_order_on_number()
print(response.status_code)