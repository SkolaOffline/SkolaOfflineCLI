import requests
import token_handler
from dataclasses import dataclass


# user class
class User:
    def __init__(self):
        # todo hardcoded for testing
        self.personid = "E2196244"
        self.school_year_id = "E22086"

    # gets data of the user
    def get_data(self):
        response = requests.get(
            "https://aplikace.skolaonline.cz/solapi/api/v1/user",
            headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        )

        # if unauthorized or bad credentials tries to get a new token from the refresh token
        if response.status_code == 401 or response.status_code == 400:
            token_handler.write_token_to_file_from_refresh_token()
            response = requests.get(
                "https://aplikace.skolaonline.cz/solapi/api/v1/user",
                headers={
                    "Authorization": f"Bearer {token_handler.get_token_from_file()}"
                },
            )
            if response.status_code == 401 or response.status_code == 400:
                raise Exception("token expired")
        # todo dalo by se udělat, když nevyjde request, aby se podíval do cache,
        # kam by se průběžně každý request ukládal

        # netuším, jak tohle funguje, ale funguje to
        data = response.json()
        data["classroom"] = data["class"]
        self.ostatni = data

        self.personid = data["personID"]
        self.school_year_id = data["schoolYearId"]
        self.modules = data["enabledModules"]
        # todo vymyslet, jak to vlastně ukládat

    # todo třeba i implementovat ten zbytek, tohle zatím stačí (snad)


def main():
    pass


if __name__ == "__main__":
    main()
