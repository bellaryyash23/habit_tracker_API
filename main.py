import os
import requests
from datetime import datetime

USERNAME = os.environ.get("USER")
TOKEN = "alfkja341l;dfs"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# POST : Request to create a new user account.
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Days of Code graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST: Request to Create a new Graph/Habit Tracker.
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

new_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2021, month=12, day=31)
today_date = today.strftime("%Y%m%d")

new_pixel_config = {
    "date": today_date,
    "quantity": "15",
}

# POST: Request to add a new Pixel of Data to the habit tracker.
# response = requests.post(url=new_pixel_endpoint, json=new_pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{new_pixel_endpoint}/{today_date}"

update_pixel_config = {
    "quantity": "8"
}

# PUT: Request to update a previously posted Pixel of data.
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{update_pixel_endpoint}"

# DELETE: Request to Delete a Pixel of Data from graph.
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
