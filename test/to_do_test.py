import requests


def test_add():
    body = {"title":"111111111", "completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]
    body = {"title":"111111111", "completed":True}
    requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 200
    assert response_body['completed'] == True


