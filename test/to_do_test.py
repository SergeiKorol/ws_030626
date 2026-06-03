import requests


def test_add(): #Иван Создать задачу, Проставить отметку о выполнении и проверить что completed ==True
    body = {"title":"111111111", "completed":False}
    """Присвоили значение переменной body"""
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]
    """Присвоили значение ID"""
    body = {"title":"111111111", "completed":True}
    requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 200
    assert response_body['completed'] == True, "Результат равен None"


