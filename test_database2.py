import pytest
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker

# Фикстура для создания соединения с базой данных
@pytest.fixture(scope="module")
def db():
    db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
    engine = create_engine(db_connection_string)
    yield engine  # Возвращаем движок для использования в тестах
    engine.dispose()  # Закрываем соединение после завершения тестов

# Фикстура для создания сессии
@pytest.fixture
def connection(db):
    connection = db.connect()
    yield connection  # Возвращаем соединение для использования в тестах
    connection.close()  # Закрываем соединение после завершения теста

# Тест для проверки соединения с базой данных
def test_db_connection(db):
    inspector = inspect(db)
    tables_names = inspector.get_table_names()
    print("Таблицы в базе данных:", tables_names)
    assert 'subject' in tables_names, "Таблица 'subject' не найдена в базе данных"

# Тест для добавления, изменения и удаления предмета
def test_insert_update_delete(connection):
    # Добавление предмета в таблицу
    with connection.begin():
        sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :new_name)")
        connection.execute(sql, {'id': 17, 'new_name': 'QA_SkyPro'})

    # Проверка, что предмет был добавлен
    with connection.begin():
        result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"), {'id': 17})
        inserted_data = result.fetchone()
        assert inserted_data is not None, "Данные не были добавлены в таблицу"
        assert inserted_data[0] == 'QA_SkyPro', "Название предмета не соответствует ожидаемому"

    # Изменение названия предмета в таблице
    with connection.begin():
        sql = text("UPDATE subject SET subject_title = :title WHERE subject_id = :id")
        connection.execute(sql, {'title': 'New title', 'id': 17})

    # Проверка, что название предмета было изменено
    with connection.begin():
        result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"), {'id': 17})
        updated_data = result.fetchone()
        assert updated_data is not None, "Данные не были обновлены"
        assert updated_data[0] == 'New title', "Название предмета не было обновлено"

    # Удаление предмета из таблицы
    with connection.begin():
        sql = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql, {"id": 17})

    # Проверка, что предмет был удален
    with connection.begin():
        result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"), {'id': 17})
        deleted_data = result.fetchone()
        assert deleted_data is None, "Данные не были удалены из таблицы"
