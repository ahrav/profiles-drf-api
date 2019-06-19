import requests


def client():
    # token_h = "Token da2ad9a8e011eefabb7c35543c24b114f53d66cb"
    data = {
        "username": "ahravvy",
        "email": "test@test.com",
        "password1": "fuckyouman",
        "password2": "fuckyouman",
    }

    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    #                          data=credentials)
    # headers = {"Authorization": token_h}
    response = requests.post(
        "http://127.0.0.1:8000/api/rest-auth/registration/", data=data
    )
    print(response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
