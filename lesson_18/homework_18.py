import requests

base_url = "https://petstore.swagger.io/"

def get_available_pet():
    """
    Gets a list of available pets
    """
    endpoint = "v2/pet/findByStatus"
    query = "status=available"
    url = f"{base_url}{endpoint}?{query}"

    try:
        response = requests.get(url)

        pets = response.json()
        if pets:
            print("Aviable pets:")
            for pet in pets:
                pet_id = pet.get('id')
                pet_name = pet.get('name')
                print(f"Pet ID: {pet_id}, Name: {pet_name}")
        else:
            print("No available pets found.")
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")

def get_all_pets():
    """
    Gets a list of all animals
    """
    endpoint = "v2/pet/findByStatus"
    query = "status=available&status=pending&status=sold"
    url = f"{base_url}{endpoint}?{query}"

    try:
        response = requests.get(url)

        pets = response.json()
        if pets:
            print("All pets:")
            for pet in pets:
                pet_id = pet.get('id')
                pet_name = pet.get('name')
                print(f"Pet ID: {pet_id}, Name: {pet_name}")
        else:
            print("No available pets found.")
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")

def add_new_pet(category_name, name, tag_name):
    """
    Add a new pet
    """
    endpoint = "v2/pet"
    url = f"{base_url}{endpoint}"
    new_pet = {
        "id": 0,
        "category": {
            "id": 0,
            "name": category_name
        },
        "name": name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": tag_name
            }
        ],
        "status": "available"
    }

    try:
        response = requests.post(url, json=new_pet)
        if response.status_code == 200:
            added_pet_info = response.json()
            added_pet_id = added_pet_info.get('id')
            print(f"Animal with category {category_name}, name {name} and ID {added_pet_id} added successfully")
        else:
             print(f"Error adding animal. Response code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")

def get_pet_by_id(pet_id):
    """
    Find pet by pet id
    """
    endpoint = "v2/pet"
    url = f"{base_url}{endpoint}/{pet_id}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            pet_info = response.json()
            print(f"Information about the animal {pet_id}:")
            print(f"Name: {pet_info['name']}, Status: {pet_info['status']}")
        else:
            print(f"Animal with ID {pet_id} not found. Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"Error during the request: {e}")

def delete_pet_by_id(pet_id):
    """
    Delete pet by pet id
    """
    endpoint = "v2/pet"
    url = f"{base_url}{endpoint}/{pet_id}"

    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print(f"Pet with ID {pet_id} deleted")
        else:
            print(f"Animal with ID {pet_id} not found. Response code: {response.status_code}")
    except requests.exceptions.RequestException as e:
            print(f"Error during the request: {e}")





get_available_pet()
get_all_pets()
add_new_pet("fish" ,"Rob", "salmon" )
get_pet_by_id(9223372036854029481)
delete_pet_by_id(9223372036854029582)