import requests
base_api_url = "https://qauto.forstudy.space/api"
s = requests.session()


class auth():

    @staticmethod
    def logout(s: requests.session, request_body: dict = {}):
        endpoint = "/auth/logout"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def signin(s: requests.session, request_body: dict):
        endpoint = "/auth/signin"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def signup(s: requests.session, request_body: dict):
        endpoint = "/auth/signup"
        return s.post(base_api_url+endpoint, json=request_body)