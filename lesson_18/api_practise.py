import requests
import random


class PetsStore():
    """
        PetsStore class provides an interface to interact with the Pet Store API.
    """
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.pets_status = ["available", "pending", "sold"]
        self.api_key = "special-key"

    """
            Retrieves a list of pets based on the specified status.
    """
    def get_all_pets(self, status="available"):
        if status not in self.pets_status:
            print("Invalid pet status. Choose from:", self.pets_status)

        endpoint = f"pet/findByStatus?status={status}"
        url = "/".join([self.base_url, endpoint])
        response = requests.get(url)

        if response.status_code == 200:
            pets = response.json()
            return pets
        else:
            print(f"Failed. Status code: {response.status_code}")

    """
        Creates a new pet with the given details.
    """
    def create_new_pet(self, name, status, category):
        endpoint = "pet"
        random_id = random.randrange(1000000, 9999999)
        url = "/".join([self.base_url, endpoint])
        headers = {
            'Content-Type': 'application/json'
        }

        r_body = {
            "id": random_id,
            "category": {
                "id": random_id,
                "name": category
            },
            "name": name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": random_id,
                    "name": name
                }
            ],
            "status": status
        }

        r = requests.post(url=url, headers=headers, json=r_body)
        if r.status_code == 200:
            print(f"New pet added: \n{r}")
        else:
            print(f"Something wrong!!! \nStatus code: {r.status_code}")
        return f"ID: {random_id}, Name: {name}, Status: {status}, Category: {category}"

    """
        Retrieves information about a pet based on its ID.
    """
    def find_by_id(self, id):
        endpoint = f"pet/{id}"
        url = "/".join([self.base_url, endpoint])
        r = requests.get(url)
        if r.status_code == 200:
            return r
        elif r.status_code == 404:
            print(f"{r.status_code}: Pet not found.\nPlease, check ID.")
        else:
            raise f"{r.status_code}: Invalid ID supplied"

    """
        Delete a pet based on its ID.
    """
    def delete_by_id(self, id):
        endpoint = f"pet/{id}"
        url = "/".join([self.base_url, endpoint])
        headers = {
            'api_key': f'{self.api_key}'}
        r = requests.delete(url, headers=headers)
        if r.status_code == 200:
            return f"Deleted: f{r}"
        elif r.status_code == 404:
            print(f"{r.status_code}: Pet not found.\nPlease, check ID.")
        else:
            raise f"{r.status_code}: Invalid ID supplied"


if __name__ == "__main__":
    pets_store = PetsStore()

    for pets in pets_store.get_all_pets("sold"):
        print(pets)

    new_pet = pets_store.create_new_pet("Bite", "available", "cat")
    print(new_pet)

    find_pet = pets_store.find_by_id(2336969)
    print(find_pet.text)

    delete_pet = pets_store.delete_by_id(8561215)
    print(delete_pet)
