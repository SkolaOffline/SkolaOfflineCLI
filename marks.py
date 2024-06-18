def get_marks_download(user):
    r = requests.get(
        f'https://aplikace.skolaonline.cz/solapi/api/v1/students/{user.personid}/marks/bySubject',
        headers={
                'Authorization': f'Bearer {token_handler.get_token_from_file()}'
            })
    return r.text


class MarksInSubject():
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.marks = []
    
    
class Mark():
    def __init__(self, mark_date, theme, markText, weight, class_average):
        self.mark_date = mark_date
        self.theme = theme
        try: self.mark_value = int(markText)
        except: self.mark_value = None
        self.weight = weight
        self.class_average = class_average




def all_marks_parser(jsn):
    jsn = json.loads(jsn)['subjects']
    # jsn = jsn[0]
    marks = []
    for subject in jsn:
        marks_in_subject = MarksInSubject(subject['subject']['name'])
        for mark in subject['marks']:
            marks_in_subject.marks.append(Mark(
                mark['markDate'],
                mark['theme'],
                mark['markText'],
                mark['weight'],
                mark['classAverage'],
            ))

        marks.append(marks_in_subject)
    return marks


if __name__ == "__main__":
    import user_handler
    import requests
    import token_handler
    import json

    # user = user_handler.User()
    # user.get_data()
    # get_marks_download(user)

    # all_marks_parser(open('marks_response.json', 'r').read())