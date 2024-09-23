from dataclasses import dataclass
import requests
import token_handler
import json


# getter známek z api, vrací json jako text (string)
def get_marks_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/students/{user.personid}/marks/bySubject",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
    )

    # if unauthorized or bad credentials tries to get a new token from the refresh token
    if r.status_code == 401 or r.status_code == 400:
        token_handler.token_login()
        r = requests.get(
            f"https://aplikace.skolaonline.cz/solapi/api/v1/students/{user.personid}/marks/bySubject",
            headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        )
        if r.status_code == 401 or r.status_code == 400:
            raise Exception(
                "Something about your login went wrong. Check your credentials."
            )

    return r.text


# class pro známky v jednotlivých předmětech
class MarksInSubject:
    def __init__(self, subject_name, marks_avg):
        self.subject_name = subject_name
        self.marks = []
        self.marks_avg = marks_avg


# class pro známku
class Mark:
    def __init__(self, mark_date, theme, markText, weight, class_average):
        self.mark_date = mark_date
        self.theme = theme
        try:
            self.mark_value = int(markText)
        except:
            self.mark_value = None
        self.weight = float(weight)
        self.class_average = class_average


# parsuje json známek
def all_marks_parser(jsn):
    jsn = json.loads(jsn)["subjects"]
    # jsn = jsn[0]
    marks = []
    for subject in jsn:
        marks_in_subject = MarksInSubject(
            subject["subject"]["name"], subject["averageText"]
        )
        for mark in subject["marks"]:
            marks_in_subject.marks.append(
                Mark(
                    mark["markDate"],
                    mark["theme"],
                    mark["markText"],
                    mark["weight"],
                    mark["classAverage"],
                )
            )

        marks.append(marks_in_subject)
    return marks


if __name__ == "__main__":
    import user_handler
    import requests
    import token_handler
    import json

    user = user_handler.User()
    user.get_data()
    # get_marks_download(user)

    print(get_marks_download(user))

    # all_marks_parser(open('marks_response.json', 'r').read())
    pass
