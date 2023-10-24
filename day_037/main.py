import requests

USERNAME = "cmattrox"
TOKEN = "asdf;1234;lkjwdf8234l;jasd"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {"date": "20230925", "quantity": "0.75"}

headers = {"X-USER-TOKEN": TOKEN}

res = requests.post(url=graph_endpoint, json=user_params, headers=headers)

print(res.text)
