import requests

def get_google():
    base_url = "https://www.google.com"
    query = {"q": "факторіал числа"}
    response = requests.get(base_url + "/search", params=query)
    print(response.status_code)
    print(response.headers)
    print(response.text[:500])

def get_olx(min_price, max_price, curr= "UAH"):
    my_query = "q-zx-spectrum"
    base_url = "https://www.olx.ua/uk/list"
    ask_url = "/".join([base_url, my_query])
    q_params = {"currency": curr,
                "search[filter_float_price:from]": min_price,
                "search[filter_float_price:to]": max_price}
    r = requests.get(ask_url, params= q_params)
    print(r.url)
    print(r.headers)
    print(r.status_code)
    print(r.text[:1200]) #  r.content

# get_olx(1000, 5000)

def get_hillel():
    url = "https://qauto.forstudy.space/api-docs/"
    r = requests.get(url, auth=("guest", "welcome2qauto"))
    print(r.url)
    print(r.headers)
    print(r.status_code)
    # url = "https://qauto.forstudy.space/api-docs/"
    # r = requests.get(url)
    # print(r.url)
    # print(r.headers)
    # print(r.status_code)


# get_hillel()

def get_kino():
    url = "https://uakino.club"
    headers = {
        "Host": "uakino.club",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }
    r = requests.get(url, headers=headers)
    print(r.url)
    print(r.headers)
    print(r.status_code)

# get_kino()
def post_uakino():
    url = "https://uakino.club"
    headers = {
        "Host": "uakino.club",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }
    data = {
        "login_name": "panix",
        "login_password": "myPa$$w0rd",
        "login": "submit"
    }

    r = requests.post(url, headers=headers, json=data)
    print("request body:", r.request.body)
    print("request headers:", r.request.headers)
    print("request url:", r.request.url)
    print("===")
    print(r.url)
    print(r.headers)
    print(r.status_code)

#post_uakino()