import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = "danithang82"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")
# getting today's date
today = datetime.now()
DATE = today.strftime("%Y%m%d")

# getting pixela website
pixela_endpoint = "https://pixe.la/v1/users"

# establishing user_params to add to url
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# json is used to call params
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph requires pixela url, username, and graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "hrs",
    "type": "int",
    "color": "ajisai",
    "timezone": "EST"
}
# adding the token to authenticate the info requested...hiding the token from the url but still authenticating
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# params for pixel value
value_params = {
    # formatting the date in the specific way we want
    "date": DATE,
    "quantity": input("How many hours did you study today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=value_params, headers=headers)

# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# update_params = {
#     "quantity": "5"
# }
# update pixel data using put request
# update_response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)

# delete requests
# delete_response = requests.delete(url=update_pixel_endpoint, headers=headers)
