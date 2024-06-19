import requests
from dataclasses import dataclass
import json
import token_handler
import time


# getuje data o absencích a vrací json jako text (string)
def get_absences_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/absences/inPeriod",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        params={
            "dateFrom": date_from(),
            "dateTo": date_to(),
        },
    )

    return r.text


# ehm harcoded datum
# todo fix
def date_from():
    return formated_date("2023-09-01")


def date_to():
    return formated_date("2024-6-30")


def formated_date(date):
    return time.strftime("%Y-%m-%dT%H:%M:%S.000", time.strptime(date, "%Y-%m-%d"))


# class pro den absencí
@dataclass
class DayOfAbsences:
    date: str
    excused: int
    unexcused: int
    notcounted: int
    unevaluated: int
    unevaluated_with_apology: int


# parsuje json absencí
def absences_parser(jsn):
    jsn = json.loads(jsn)["absences"]
    absences = {}
    for day in jsn:
        absences[day["date"]] = DayOfAbsences(
            day["date"],
            day["numberOfExcused"],
            day["numberOfUnexcused"],
            day["numberOfNotCounted"],
            day["numberOfUnevaluated"],
            day["numberOfUnevaluatedWithApology"],
        )

    return absences


if __name__ == "__main__":
    pass
    # import user_handler
    # import requests
    # import token_handler
    # import json
    # import datetime
    # import time

    # user = user_handler.User()
    # user.get_data()
    # absences_parser(get_absences_download(user))
