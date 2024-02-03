import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def get_pets(status):
    base_url = "https://petstore.swagger.io"
    query = "v2/pet/findByStatus"
    ask_query = "/".join([base_url, query])
    param = {"status": status}
    response = requests.get(ask_query, param)
    print(response.content)
get_pets("avaliable")
print("**"*66)


"""Додати нову тварину (метод POST)"""

def add_pet(pet_info):
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=pet_info)
    print("Тварину створено, ось її дані", response.content)

pet_info = {"name": "Бантик", "status": "available"}    
add_pet(pet_info)

"""Знайти тварину за ідентифікатором (метод GET)."""
def get_pets_id():
    id = input("введіть ідентифікатор: ")
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    response = requests.get(url)
    print(response.content)
get_pets_id()

"""Видалити тварину за ідентифікатором (метод DELETE)"""
def delete_pet():
    id = input("введіть ідентифікатор: ")
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("тварина тепер в кращому світі")
    else: print(response.status_code)


