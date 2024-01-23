import requests


def get_by_avaliable_status():
    """get avaliable pets"""
    url = "https://petstore.swagger.io/v2/pet/"
    status_avaliable = "status=available"
    response = requests.get(url + "findByStatus", status_avaliable)
    print(f"Searching for pets with status: avaliable")
    print(response.status_code)
    print(response.headers)
    print(response.text[:400])


# post
def post_patron():
    """Creates dog Patron with id:65123"""
    url = "https://petstore.swagger.io/v2/pet"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    }
    data = {
        "id": 65123,
        "category": {
            "id": 65123,
            "name": "Патрон"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 65123,
                "name": "Патрон"
            }
        ],
        "status": "available"
    }

    r = requests.post(url, headers=headers, json=data)
    print(f"Animal with id:65123 is created")
    print("request body:", r.request.body)
    print("request headers:", r.request.headers)
    print("request url:", r.request.url)
    print(r.url)
    print(r.headers)
    print(r.status_code)


def get_patron():
    """Searches for pet with id:65123"""
    url = "https://petstore.swagger.io/v2/pet/"
    id = "65123"
    response = requests.get(url + id)
    print(f"Animal with id:{id} is searched")
    print(response.status_code)
    print(response.headers)
    print(response.text[:500])


def delete_patron():
    """Deletes pet with id:65123"""
    url = "https://petstore.swagger.io/v2/pet/"
    id = "65123"
    response = requests.delete(url + id)
    print(f"Animal with id:{id} deleted")
    print(response.status_code)
    print(response.headers)
    print(response.text[:500])


get_by_avaliable_status()
post_patron()
get_patron()
delete_patron()
get_patron()  # to make sure that patron deleted
