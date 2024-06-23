import requests
from dataclasses import dataclass
import json
import token_handler
import time
import datetime


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
    # if unauthorized or bad credentials tries to get a new token from the refresh token
    if r.status_code == 401 or r.status_code == 400:
        token_handler.write_token_to_file_from_refresh_token()
        r = requests.get(
            f"https://aplikace.skolaonline.cz/solapi/api/v1/absences/inPeriod",
            headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
            params={
                "dateFrom": date_from(),
                "dateTo": date_to(),
            },
        )
        if r.status_code == 401 or r.status_code == 400:
            raise Exception("token expired")

    return r.text


# ehm harcoded datum
# todo fix
def date_from():
    today = datetime.date.today()
    if today.month < 9 and today.month > 2:  # Second half of the year
        second_semester = datetime.date(today.year, 2, 1)
        return formated_date(second_semester.strftime("%Y-%m-%d"))
    else:
        first_semester = datetime.date(today.year, 9, 1)
        return formated_date(first_semester.strftime("%Y-%m-%d"))


# vrací datum příštího pátku ve vhodném formátu pro api
def date_to():
    today = datetime.date.today()
    return formated_date(today.strftime("%Y-%m-%d"))


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


@dataclass
class AbsencesInSubject:
    subject_name: str
    absences: int
    percentage: float
    number_of_hours: int
    excused: int
    unexcused: int
    notcounted: int
    unevaluated: int
    unevaluated_with_apology: int
    allowed_absences: int
    allowed_percentage: float


# parsuje json absencí
def absences_parser(jsn, subjects_absence):
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

    for subject in subjects_absence:
        absences_in_subject = AbsencesInSubject(
            subject["subject"]["name"],
            subject["absenceAll"],
            subject["absenceAllPercentage"],
            subject["numberOfHours"],
            subject["numberOfExcused"],
            subject["numberOfUnexcused"],
            subject["numberOfNotCounted"],
            subject["numberOfUnevaluated"],
            subject["numberOfUnevaluatedWithApology"],
            subject["allowedAbsence"],
            subject["allowedAbsencePercentage"],
        )
        absences[subject["subject"]["name"]] = absences_in_subject

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
