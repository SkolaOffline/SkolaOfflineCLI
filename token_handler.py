import requests
import logging


def get_token(uzivatel, heslo):
    response = requests.post(
        "https://aplikace.skolaonline.cz/solapi/api/connect/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "password",
            "username": uzivatel,
            "password": heslo,
            "client_id": "test_client",
            "scope": "openid offline_access profile sol_api",
        },
    )

    if response.status_code == 401:
        raise Exception("Nesprávné uživatelské jméno nebo heslo")
    elif response.status_code == 400:
        logging.warning("Token expired, trying to get new one from refresh token")
        response = get_refresh_token_from_file()

    if response.status_code != 200:
        raise Exception(f"{response.status_code} ({response.text})")

    access_token = response.json()["access_token"]
    refresh_token = response.json()["refresh_token"]
    print(f'token expires in: {response.json()["expires_in"]}')

    return access_token, refresh_token


def get_token_from_refresh_token():
    refresh_token = get_refresh_token_from_file()
    response = requests.post(
        "https://aplikace.skolaonline.cz/solapi/api/connect/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": "test_client",
            "scope": "offline_access sol_api",
        },
    )

    if response.status_code != 200:
        raise Exception(f"{response.status_code} ({response.text})")

    return response


def write_token_to_file(uzivatel, heslo):
    access_token, refresh_token = get_token(uzivatel, heslo)
    open("token", "w").write(access_token + "\n" + refresh_token)


def token_login():
    uzivatel, heslo = open("credentials", "r").readlines()

    write_token_to_file(uzivatel, heslo)


def get_token_from_file():
    return open("token", "r").read().split("\n")[0]


def get_refresh_token_from_file():
    return open("token", "r").read().split("\n")[1]
