# tests/test_user_api.py

import pytest
from api_client import APIClient

client = APIClient()

def test_get_country():
    response = client.get("/name/deutschland")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"]["common"] == "Germany"
    assert data[0]["region"] == "Europe"

# # def test_get_user():
#     # Testing a GET request for a specific user
#     response = client.get("/users/1")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == 1
#     assert data["name"] == "Leanne Graham"

# def test_create_user():
#     # Testing a POST request to create a new user
#     new_user = {
#         "name": "John Doe",
#         "username": "johndoe",
#         "email": "john.doe@example.com"
#     }
#     response = client.post("/users", data=new_user)
#     assert response.status_code == 201
#     data = response.json()
#     assert data["name"] == "John Doe"
#     assert data["username"] == "johndoe"

# def test_update_user():
#     # Testing a PUT request to update an existing user
#     updated_user = {
#         "name": "Jane Doe",
#         "username": "janedoe"
#     }
#     response = client.put("/users/1", data=updated_user)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "Jane Doe"
#     assert data["username"] == "janedoe"

# def test_delete_user():
#     # Testing a DELETE request to remove a user
#     response = client.delete("/users/1")
#     assert response.status_code == 200

