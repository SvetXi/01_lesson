import pytest
import requests

# Базовый URL API
BASE_URL = "https://yougile.com"

# Токен для авторизации (замените на ваш реальный токен)
API_TOKEN = "aqZdCow0hA3q8SC7AeSDxS1MYYNT93yO1GG5gBV2xGwHUYq3hmU1gVI8OU7bvfLh"

# Заголовки для запросов
HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}


# Фикстура для создания проекта, который будет использоваться в тестах
@pytest.fixture(scope="session")
def create_project():
    project_data = {
         'title': 'Новый проект',
    }
    response = requests.post( BASE_URL + '/api-v2/projects', json=project_data, headers=HEADERS)
    assert response.status_code == 201
    project_id = response.json()["id"]
    yield project_id
    # Удаление проекта после выполнения теста
    #requests.delete(BASE_URL + '/projects/{project_id}', headers=HEADERS)

# Позитивный тест для создания проекта
def test_create_project_positive():
    project_data = {
        'title': 'Новый проект',
    }
    response = requests.post(BASE_URL + '/api-v2/projects', json=project_data, headers=HEADERS)
    assert response.status_code == 201
    assert "id" in response.json()

# Негативный тест для создания проекта (отсутствие обязательного поля)
def test_create_project_negative():
    project_data = {
        "users": "This project has no title"
    }
    response = requests.post(BASE_URL + '/api-v2/projects', json=project_data, headers=HEADERS)
    assert response.status_code == 400

# Позитивный тест для получения списка проектов
def test_get_projects_positive():
    response = requests.get(BASE_URL + '/api-v2/projects',headers=HEADERS)
    assert response.status_code == 200
    #assert isinstance(response.json(), list)
    assert "content" in response.json()
    assert isinstance(response.json()["content"], list)

# Позитивный тест для получения проекта по id
def test_get_project_positive(create_project):
    project_id = create_project
    response = requests.get(BASE_URL + f'/api-v2/projects/{project_id}', headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["id"] == project_id
    assert "id" in response.json()


# Негативный тест для получения несуществующего проекта
def test_get_project_negative():
    non_existent_id = "non_existent_id"
    response = requests.get(BASE_URL + f'/api-v2/projects/{non_existent_id}', headers=HEADERS)
    assert response.status_code == 404

# Позитивный тест для обновления проекта
def test_update_project_positive(create_project):
    project_id = create_project
    update_data = {
        'title': 'Обновление проекта'
    }
    response = requests.put(BASE_URL + f'/api-v2/projects/{project_id}', headers=HEADERS)
    assert response.status_code == 200
    assert "id" in response.json()


# Негативный тест для обновления проекта (отсутствие обязательного поля)
def test_update_project_negative(create_project):
    project_id = create_project
    update_data = {
        'title': 'Обновление проекта'
    }
    response = requests.put(BASE_URL + f'/api-v2/projects/',  headers=HEADERS)
    assert response.status_code == 404
