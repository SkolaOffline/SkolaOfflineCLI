import requests
import token_handler
import json
from datetime import datetime
from dataclasses import dataclass


def get_marks(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/students/{user.personid}/marks/list",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
    )
    marks_list = marks_parser(r.text)
    return marks_list


def marks_parser(marks_json):
    marks_data = json.loads(marks_json)
    marks_list = []

    for mark_item in marks_data["marks"]:
        mark = Mark()
        mark.mark_date = datetime.strptime(
            mark_item["markDate"], "%Y-%m-%dT%H:%M:%S"
        ).strftime("%d/%m/%Y")
        mark.theme = mark_item["theme"]
        mark.mark_text = mark_item["markText"]
        mark.weight = mark_item["weight"]

        for subject in marks_data["subjects"]:
            if subject["id"] == mark_item["subjectId"]:
                mark.subject_abbr = subject["abbrev"]
                mark.subject_name = subject["name"]
                break

        mark.index_number = len(marks_list) + 1

        marks_list.append(mark)

    return marks_list


@dataclass
class Mark:
    mark_date: str = None
    theme: str = None
    mark_text: str = None
    weight: float = None
    subject_abbr: str = None
    subject_name: str = None
    index_number: int = None


@dataclass
class Mark_Extended:
    teacher_abbrev: str = None
    teacher_name: str = None
    subject_abbrev: str = None
    subject_name: str = None
    theme: str = None
    mark_date: str = None
    mark_text: str = None
    weight: float = None
    comment: str = None
    class_rank_text: str = None
    class_average: str = None


def main():
    pass


#
#
if __name__ == "__main__":
    main()
