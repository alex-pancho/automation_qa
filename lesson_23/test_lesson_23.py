import logging
import pytest

# Конфігурація логера
# logging.basicConfig(level=logging.INFO)
# @pytest.fixture()
# def resource():
#     print("setup")
#     yield "resource"
#     print("teardown")

class DBConnection():
    count = 0

    def __init__(self) -> None:
        self.__class__.count = self.count + 1
        self.connection = "You connect to Pentagon DB"

    def __repr__(self) -> str:
        return f"{self.connection} {self.count}"

@pytest.fixture()  # autouse=True   # scope="module"
def connect_to_database():
    connection = DBConnection()
    # assert connection == 0  ## ERROR
    return connection

# Тестова функція
def test_example(connect_to_database):
    logging.info(connect_to_database)
    # Робота тесту
    assert 1 + 1 == 2

# Запуск тесту
if __name__ == "__main__":
    pytest.main()
