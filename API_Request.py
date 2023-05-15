# Part 1:
# Create User: Create new user, return created user data.
# POST: /user/create
url = "https://dummyapi.io/data/v1/user/create"

headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}
payload = {
   "firstName": "Chang",
   "lastName": "Leo",
   "email": "dillontsvs@gmail.com"
}

response = requests.request("POST", url, headers=headers, json=payload)
assert response.status_code == 200, f"{response.status_code}"
data = response.json()
user_id = data['id']
''''''
# Part 2:
# Delete User: Delete user by id, return id of deleted user
# DELETE: /user/:id
url = f"https://dummyapi.io/data/v1/user/%7Buser_id%7D"

headers = {
  'app-id': '63eb435ad8bb0b7ee5b67a77'
}
payload = {
  'id': f'{user_id}'
}

response = requests.request("POST", url, headers=headers, json=payload)
assert response.status_code == 200, f"{response.status_code}"

# Part 3:
# Create Post: Create new post, return created post data.
# POST: /post/create
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