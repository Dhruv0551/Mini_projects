import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "enter_your_username"
token = "enter_your_token"

header = {
    "X-USER-TOKEN": token
}

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_params = {
    "id": "g01",
    "name": "ML Graph",
    "unit": "commits",
    "type": "int",
    "color": "ajisai"
}

# Uncomment to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Uncomment to create graph
# graph = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(graph.text)

current_date = str(datetime.now().date()).replace("-", "")

graph_post_endpoint = f"{pixela_endpoint}/{username}/graphs/g01"
graph_put_endpoint = f"{pixela_endpoint}/{username}/graphs/g01/{current_date}"

graph_post_params = {
    "date": current_date,
    "quantity": input("How many commits did you make today? ")
}

graph_add_request = requests.put(url=graph_post_endpoint, json=graph_post_params, headers=header)
print(graph_add_request.text)
