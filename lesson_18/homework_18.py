import requests
import random

BASE_URL = 'https://petstore.swagger.io/v2'
API_KEY = 'special-key'


def get_pets(status='available'):
    """
    This function for get all pets from petstore.swagger with necessary status.
    Default: available
    """
    url = f"{BASE_URL}/pet/findByStatus"
    q_url = f"{url}?status={status.lower()}"

    response = requests.get(q_url)
    pets = response.json()
    if response.status_code == 200:
        pet_list = []
        for pet in pets:
            pet_template = f"Pet ID: {pet['id']}, Name: {pet['name']}, Status: {pet['status']}"
            pet_list.append(pet_template)

        return '\n'.join(pet_list)
    else:
        return f"Message: {response.json().get('message')}. Status code: {response.status_code}."


def post_new_pet(name: str, photo_urls='string', status='available'):
    """
    This function for posting new pets to petstore.swagger
    """
    url = f"{BASE_URL}/pet"
    headers = {'Content-Type': 'application/json'}
    data = {"id": random.randint(1000, 10000),
            "category": {"id": 0, "name": "string"},
            "name": name,
            "photoUrls": [photo_urls],
            "tags": [{"id": 0, "name": "string"}],
            "status": status}
    response = requests.post(url=url, json=data, headers=headers)
    return f"Response: {response.json()}.\nStatus code: {response.status_code}"


def get_pet_by_id(pet_id: int):
    """
    This function for getting pet by ID from petstore.swagger
    """
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    pets = response.json()
    if response.status_code == 200:
        pet_template = f"Pet ID: {pets['id']}, Name: {pets['name']}, Status: {pets['status']}"
        return pet_template
    else:
        return f"Message: {response.json().get('message')}. Status code: {response.status_code}."


def delete_pet_by_id(pet_id: int, api_key):
    """
    This function for deleting pet by ID from petstore.swagger
    """
    url = f"{BASE_URL}/pet/{pet_id}"
    headers = {
        'Content-Type': 'application/json',
        'api_key': api_key
    }
    response = requests.delete(url=url, headers=headers)

    if response.status_code == 200:
        return f"Pet was deleted successfully! Response: {response.json()}"
    elif response.status_code == 400:
        return "Invalid ID supplied"
    elif response.status_code == 404:
        return "Pet not found"


if __name__ == '__main__':
    print(get_pets())
    # Pet ID: 37750, Name: Fermin, Status: available
    # Pet ID: 21617, Name: Stacey, Status: available
    # Pet ID: 15826, Name: Cornelius, Status: available
    # ...
    # Pet ID: 513598762413800256, Name: Norbert, Status: available

    print(post_new_pet('Serega', status='pending'))
    # Response: {'id': 5941, 'category': {'id': 0, 'name': 'string'}, 'name': 'Serega', 'photoUrls': ['string'],
    # 'tags': [{'id': 0, 'name': 'string'}], 'status': 'pending'}. Status code: 200

    print(get_pet_by_id(10))
    # Pet ID: 10, Name: doggie, Status: available
    print(get_pet_by_id(222222222222))
    # Message: Pet not found. Status code: 404.

    print(delete_pet_by_id(5, API_KEY))
    # Pet was deleted successfully! Response: {'code': 200, 'type': 'unknown', 'message': '5'}
