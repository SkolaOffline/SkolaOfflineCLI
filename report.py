import requests
import token_handler
from dataclasses import dataclass
import json


def get_report_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/students/{user.personid}/marks/final",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
    )

    # if unauthorized or bad credentials tries to get a new token from the refresh token
    if r.status_code == 401 or r.status_code == 400:
        token_handler.token_login()
        r = requests.get(
            f"https://aplikace.skolaonline.cz/solapi/api/v1/students/{user.personid}/marks/final",
            headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        )
        if r.status_code == 401 or r.status_code == 400:
            raise Exception(
                "Something about your login went wrong. Check your credentials."
            )

    return r.text


# class for mark in report
@dataclass
class FinalMark:
    subject_name: str
    mark: str


@dataclass
class Grade:
    marks: list[FinalMark]
    grade_name: str
    year: str
    semester: str
    closed: bool
    achievment_text: str
    average: float
    absent_hours: int
    excused_hours: int
    unexcused_hours: int


def report_parser(jsn):
    # Directly access "certificateTerms" from the dictionary
    jsn = json.loads(jsn)["certificateTerms"]
    grades = []
    for grade in jsn:
        # Create a mapping of subject IDs to names for easier lookup
        subject_id_to_name = {
            subject["id"]: subject["name"] for subject in grade["subjects"]
        }

        marks = []
        for mark in grade["finalMarks"]:
            # Use the mapping to find the subject name by ID
            subject_name = subject_id_to_name.get(mark["subjectId"], "Unknown")
            marks.append(FinalMark(subject_name, mark["markText"]))
        grades.append(
            Grade(
                marks,
                grade["gradeName"],
                grade["schoolYearName"],
                grade["semesterName"],
                grade["closed"],
                grade["achievementText"],
                grade["marksAverage"],
                grade["absentHours"],
                grade["excusedHours"],
                grade["notExcusedHours"],
            )
        )
    return grades


if __name__ == "__main__":
    # import printy

    # with open("report_response.json", "r", encoding="utf-8") as file:
    #     json_data = json.load(file)

    # # Pass the loaded JSON data to the report_parser function
    # printy.print_report(report_parser(json_data))

    pass
