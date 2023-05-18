import requests
import json

#part1
url = "https://dummyapi.io/data/v1/user/create"
headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}
payload = {
   "firstName": "chang",
   "lastName": "leo",
   "email": "dillontsvs@gmail.com"
}

response = requests.request("POST", url, headers=headers, json=payload)
assert response.status_code == 200, f"{response.status_code}"
data = response.json()
user_id = data['id']

#=============================
#part2
url = f"https://dummyapi.io/data/v1/user/{user_id}"

headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}
payload = {
  'id': f'{user_id}'
}

response = requests.request("DELETE", url, headers=headers, json=payload)
assert response.status_code == 200, f"{response.status_code}"

#=============================
#part3
url = "https://dummyapi.io/data/v1/post/create"

headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}
payload = {
    "text": "testtest preview only",
    "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FImage&psig=AOvVaw3LEOhYgNYdkQBaqUl4SGZ3&ust=1684237155109000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMDV7f2e9_4CFQAAAAAdAAAAABAE",
    "likes": 2,
    "tags": "['1', '2']",
    "owner": f"{user_id}"
}

response = requests.request("POST", url, headers=headers, json=payload)
data = response.json()
assert response.status_code == 200, f"{response.status_code}"
print(data)

#=============================
#Part4
url = f"https://dummyapi.io/data/v1/user/{user_id}/post"

headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}
response = requests.request("GET", url, headers=headers, json=payload)
data = response.json()
assert response.status_code == 200, f"{response.status_code}"
print(data)

#=============================
#Part5
url = f"https://dummyapi.io/data/v1/user/{user_id}"
headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}

response = requests.request("DELETE", url, headers=headers, json=payload)
assert response.status_code == 200, f"{response.status_code}"
print(response)