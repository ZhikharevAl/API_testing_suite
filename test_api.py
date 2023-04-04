import requests


def test_create_user():
    # отправляем POST-запрос для создания нового пользователя
    response = requests.post('https://reqres.in/api/users', data={
        'name': 'Jesse Pinkman',
        'job': 'Software Engineer'
    })
    # проверяем, что код ответа равен 201 (Created)
    assert response.status_code == 201

    # распечатываем ответ в консоли
    print(response.json())

    # проверяем, что в ответе есть ID созданного пользователя
    assert 'id' in response.json()


def test_update_user():
    # отправляем PUT-запрос для изменения данных пользователя
    response = requests.put('https://reqres.in/api/users/2', data={
        'name': 'Jesse Pinkman',
        'job': 'Software Developer'
    })

    # проверяем, что код ответа равен 200 (OK)
    assert response.status_code == 200

    print(response.json())

    # проверяем, что в ответе есть данные измененного пользователя
    assert response.json()['name'] == 'Jesse Pinkman'
    assert response.json()['job'] == 'Software Developer'


def test_delete_user():
    # отправляем GET-запрос, чтобы получить список всех пользователей
    response = requests.get('https://reqres.in/api/users')
    user_list = response.json()['data']
    user_id = None
    for user in user_list:
        if user['id'] == 2:
            user_id = 2
            break
    assert user_id is not None, "User with id=2 doesn't exist"

    # отправляем DELETE-запрос для удаления пользователя
    response = requests.delete(f'https://reqres.in/api/users/{user_id}')

    # проверяем, что код ответа равен 204 (No Content)
    assert response.status_code == 204


def test_single_user():
    # Тест на получение данных о конкретном пользователе
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["last_name"] == "Weaver"


def test_list_resources():
    # Тест на получение списка ресурсов
    response = requests.get(f"{'https://reqres.in/api'}/unknown")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert len(data["data"]) == 6


def test_single_resource():
    # Тест на получение данных о конкретном ресурсе
    response = requests.get(f"{'https://reqres.in/api'}/unknown/2")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["data"]["id"] == 2
    assert data["data"]["name"] == "fuchsia rose"
    assert data["data"]["year"] == 2001
    assert data["data"]["color"] == "#C74375"
