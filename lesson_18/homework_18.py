import http
import requests

# URL Swagger Petstore API
base_url = "https://petstore.swagger.io/v2/pet"


# Getting a list of available animals (GET method)
def get_available_pets():
    response = requests.get(f"{base_url}/findByStatus", params={"status": "available"})
    if response.status_code != http.HTTPStatus.OK:
        raise Exception("Something went wrong with the request: " + str(response.status_code))
    pets = response.json()
    return pets


# Adding a new animal (POST method)
def add_new_pet(pet_data):
    response = requests.post(base_url, json=pet_data)
    if response.status_code != http.HTTPStatus.OK:
        raise Exception("Something went wrong with the request: " + str(response.status_code))
    pet_json = response.json()
    return pet_json


# Finding an animal by ID (GET method)
def find_pet_by_id(pet_id):
    response = requests.get(f"{base_url}/{pet_id}")
    if response.status_code != http.HTTPStatus.OK:
        raise Exception("Something went wrong with the request: " + str(response.status_code))
    pet_info = response.json()
    return pet_info


# Deleting an animal by ID (DELETE method)
def delete_pet_by_id(pet_id):
    response = requests.delete(f"{base_url}/{pet_id}")
    if response.status_code != http.HTTPStatus.OK:
        raise Exception("Something went wrong with the request: " + str(response.status_code))
    pet_deletion_status = response.json()
    return pet_deletion_status


# Getting and displaying the list of available animals
available_pets = get_available_pets()
print("Список доступних тварин:")
for pet in available_pets:
    print(f"ID: {pet['id']}, Ім'я: {pet['name'] if 'name' in pet else ''}, Статус: {pet['status']}")

# Adding a new animal and displaying confirmation on the screen
pet_data = {"name": "Барсик", "status": "available"}
new_pet = add_new_pet(pet_data)
print(f"\n Нова тварина додана. Підтвердження: {new_pet}")

# Finding an animal by ID and displaying information on the screen
pet_id_to_find = new_pet['id']
found_pet_info = find_pet_by_id(pet_id_to_find)
print(f"\n Інформація про тварину з ID {pet_id_to_find}:")
print(found_pet_info)

# Deleting an animal by ID and displaying the deletion status on the screen
pet_id_to_delete = pet_id_to_find
deletion_status = delete_pet_by_id(pet_id_to_delete)
print(f"\n Статус видалення тварини з ID {pet_id_to_delete}: {deletion_status}")
