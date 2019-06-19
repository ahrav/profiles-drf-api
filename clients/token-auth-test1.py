import requests


def client():
    token_h = "Token da2ad9a8e011eefabb7c35543c24b114f53d66cb"
    # credentials = {'username': 'ahrav', 'password': 'password'}

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #                          data=credentials)
    headers = {"Authorization": token_h}
    response = requests.get(
        "http://127.0.0.1:8000/api/v1/profiles/", headers=headers
    )
    print(response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
