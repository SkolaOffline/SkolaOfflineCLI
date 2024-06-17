import requests
import token_handler
import time
import datetime
import json
from dataclasses import dataclass

def date_from():
    today = datetime.date.today()
    if today.weekday() >= 5:  # Saturday or Sunday
        next_monday = today + datetime.timedelta(days=(7 - today.weekday()))
        return formated_date(next_monday.strftime('%Y-%m-%d'))
    else:
        last_monday = today - datetime.timedelta(days=today.weekday())
        return formated_date(last_monday.strftime('%Y-%m-%d'))
    
def date_to():
    today = datetime.date.today()
    next_friday = today + datetime.timedelta(days=(4 - today.weekday() + 7) % 7)
    return formated_date(next_friday.strftime('%Y-%m-%d'))

def formated_date(date):
    return time.strftime('%Y-%m-%dT%H:%M:%S.000', time.strptime(date, '%Y-%m-%d'))

def get_timetable(user):
    r = requests.get(
        'https://aplikace.skolaonline.cz/solapi/api/v1/timeTable',
        params = {
            'studentId': user.personid,
            'dateFrom': date_from(),
            'dateTo': date_to(),
            'schoolYearId': user.school_year_id
            },
        headers={
                'Authorization': f'Bearer {token_handler.get_token_from_file()}'
            })

    print(r.status_code)
    timetable = timetable_week_parser(r.text)
    
    return timetable

def timetable_week_parser(timetable):
    timetable = json.loads(timetable)
    monday      = timetable_day_parser(timetable['days'][0])
    tuesday     = timetable_day_parser(timetable['days'][1])
    wednesday   = timetable_day_parser(timetable['days'][2])
    thursday    = timetable_day_parser(timetable['days'][3])
    friday      = timetable_day_parser(timetable['days'][4])

    return [monday, tuesday, wednesday, thursday, friday]

def timetable_day_parser(day):
    day = day['schedules']
    lessons = []
    for lesson in day:
        less = lesson_parser(lesson)
        if less.lesson_type == 'SUPLOVANA':
            continue
        lessons.append(less)

    return lessons

@dataclass
class Lesson():
    lesson_from: str        = None
    lesson_to: str          = None
    lesson_type: str        = None
    subject_abbrev: str     = None
    subject_name: str       = None
    classroom: str          = None
    teacher: str            = None
    lesson_order: int       = None
    lesson_title: str       = None
    lesson_description: str = None


def lesson_parser(hodina):
    lesson = Lesson()
    if hodina['hourType']['id'] == 'SKOLNI_AKCE':
        lesson.lesson_type = 'SKOLNI_AKCE'
        lesson.lesson_from = hodina['lessonIdFrom']
        lesson.lesson_to = hodina['lessonIdTo']
        lesson.lesson_title = hodina['title']
        lesson.lesson_description = hodina['description']

        return lesson
        
    print(hodina)
    print('\n\n\n\n\n')
    lesson.lesson_from = hodina['lessonIdFrom']
    lesson.lesson_to = hodina['lessonIdTo']
    lesson.lesson_type = hodina['hourType']['id']
    lesson.subject_abbrev = hodina['subject']['abbrev']
    lesson.subject_name = hodina['subject']['name']
    lesson.classroom = hodina['rooms'][0]['name'] # may (and will) fuck up [0]
    lesson.teacher = hodina['teachers'][0]['displayName'] # -//-
    lesson.lesson_order = hodina['detailHours'][0]['order'] #-//-

    return lesson







class delUser():
    def __init__(self):
        self.personid = "E2196244"
        self.school_year_id = "E22086"

def main():
    # timetable = timetable_week_parser(open('timetable_response.json', 'r').read())
    # for x, day in enumerate(timetable):
    #     # print(day)
    #     for lesson in timetable[x]:
    #         print(lesson.subject_abbrev, end='\t')

    #     print()
    pass
    # user = delUser()
    # print('Timetable')
    # out = get_timetable(user)
    # print(out)



if __name__ == '__main__':
    main()