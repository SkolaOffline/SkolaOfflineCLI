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
<<<<<<< HEAD
        token_handler.write_token_to_file_from_refresh_token()
=======
        token_handler.token_login()
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31
        r = requests.get(
            f"https://aplikace.skolaonline.cz/solapi/api/v1/absences/inPeriod",
            headers={
                "Authorization": f"Bearer {token_handler.get_token_from_refresh_token()}"
            },
            params={
                "dateFrom": date_from(),
                "dateTo": date_to(),
            },
        )
        if r.status_code == 401 or r.status_code == 400:
<<<<<<< HEAD
            raise Exception("token expired")
=======
            raise Exception(
                "Something about your login went wrong. Check your credentials."
            )
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31

    return r.text


def get_absences_in_subjects_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/absences/inSubject",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        params={
            "dateFrom": date_from(),
            "dateTo": date_to(),
        },
    )
    # if unauthorized or bad credentials tries to get a new token from the refresh token
    if r.status_code == 401 or r.status_code == 400:
<<<<<<< HEAD
        token_handler.write_token_to_file_from_refresh_token()
=======
        token_handler.token_login()
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31
        r = requests.get(
            f"https://aplikace.skolaonline.cz/solapi/api/v1/absences/inSubject",
            headers={
                "Authorization": f"Bearer {token_handler.get_token_from_refresh_token()}"
            },
            params={
                "dateFrom": date_from(),
                "dateTo": date_to(),
            },
        )
        if r.status_code == 401 or r.status_code == 400:
<<<<<<< HEAD
            raise Exception("token expired")
=======
            raise Exception(
                "Something about your login went wrong. Check your credentials."
            )
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31

    return r.text


# vrací datum podle toho, jestli je druhé pololetí nebo první
def date_from():
    today = datetime.date.today()
    if today.month < 9 and today.month > 2:  # Second half of the year
        second_semester = datetime.date(today.year, 2, 1)
        return formated_date(second_semester.strftime("%Y-%m-%d"))
    else:
        first_semester = datetime.date(today.year, 9, 1)
        return formated_date(first_semester.strftime("%Y-%m-%d"))


# vrací dnešní datum
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
class Absences:
    absences: int
    hours: int
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
    # unevaluated: int
    # unevaluated_with_apology: int
    allowed_absences: int
    allowed_percentage: float


# parsuje json absencí
def absences_parser(jsn, jsn2):
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

    data = json.loads(jsn2)

    # Parsing individual subjects
    absences_in_subject = {}
    for subject_info in data["subjects"]:
        subject = subject_info["subject"]
        subject_key = subject["name"]
        absences_in_subject[subject_key] = AbsencesInSubject(
            subject_name=subject["name"],
            absences=subject_info["absenceAll"],
            percentage=subject_info["absenceAllPercentage"],
            number_of_hours=subject_info["numberOfHours"],
            excused=subject_info["numberOfExcused"],
            unexcused=subject_info["numberOfUnexcused"],
            notcounted=subject_info["numberOfNotCounted"],
            # unevaluated=subject_info["numberOfUnevaluated"],
            # unevaluated_with_apology=subject_info["numberOfUnevaluatedWithApology"],
            allowed_absences=(
                subject_info["allowedAbsence"]
                if subject_info["allowedAbsence"] is not None
                else 0
            ),  # Handling null values
            allowed_percentage=(
                subject_info["allowedAbsencePercentage"]
                if subject_info["allowedAbsencePercentage"] is not None
                else 0.0
            ),  # Handling null values
        )

    # Extracting summary information
    summary = Absences(
        absences=data["summaryAbsenceAll"],
        hours=data["summaryNumberOfHours"],
        excused=data["summaryNumberOfExcused"],
        unexcused=data["summaryNumberOfUnexcused"],
        notcounted=data["summaryNumberOfNotCounted"],
        unevaluated=data["summaryNumberOfUnevaluated"],
        unevaluated_with_apology=data["summaryNumberOfUnevaluatedWithApology"],
    )

    return absences, absences_in_subject, summary


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
