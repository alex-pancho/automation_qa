from requests import Session


def get_hillel():
    my_session = Session()
    url = "https://qauto.forstudy.space/api-docs/"
    my_session.auth=("guest", "welcome2qauto")
    r = my_session.get(url)
    print(r.url)
    print(r.headers)
    print(r.cookies)
    print(r.status_code)
    url = "https://qauto.forstudy.space/api-docs/"
    r = my_session.get(url)
    print(r.url)
    print(r.headers)
    print(r.cookies)
    print(r.status_code)


get_hillel()
