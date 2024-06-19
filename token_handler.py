import requests
import logging


# získání tokenu
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
        response = get_token_from_refresh_token()
        # pokusí se získat nový token z refresh tokenu

    if response.status_code != 200:
        raise Exception(f"{response.status_code} ({response.text})")

    # gets the token and refresh token from the response json
    access_token = response.json()["access_token"]
    refresh_token = response.json()["refresh_token"]
    print(f'token expires in: {response.json()["expires_in"]}')

    # returns the tokens
    return access_token, refresh_token


# tries to get a new token from the refresh token
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

    access_token = response.json()["access_token"]
    refresh_token = response.json()["refresh_token"]

    return access_token, refresh_token


# writes both tokens to a file called token, gets the tokens from the get_token() function independently
def write_token_to_file(uzivatel, heslo):
    access_token, refresh_token = get_token(uzivatel, heslo)
    open("token", "w").write(access_token + "\n" + refresh_token)


# writes both tokens to a file called token, gets the tokens from the get_token_from_refresh_token() function independently
def write_token_to_file_from_refresh_token():
    access_token, refresh_token = get_token_from_refresh_token()
    open("token", "w").write(access_token + "\n" + refresh_token)


# tries to login using credentials and writes the tokens to a file
def token_login():
    uzivatel, heslo = open("credentials", "r").readlines()
    write_token_to_file(uzivatel, heslo)


# tries to login using refresh token and writes the tokens to a file
def refresh_login():
    refresh_token = open("token", "r").read().split("\n")[1]
    write_token_to_file_from_refresh_token()


# returns the access token from the file
def get_token_from_file():
    return open("token", "r").read().split("\n")[0]


# returns the refresh token from the file
def get_refresh_token_from_file():
    return open("token", "r").read().split("\n")[1]
