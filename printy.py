from tabulate import tabulate
import pyfiglet
import datetime
import messages
from bs4 import BeautifulSoup

# třída pro printování


def print_modules(modules):
    for x, module in enumerate(modules):
        module = module["module"]
        print(f"{x}: {module['moduleId']:<10}")
        # print(f"{x}: {module['moduleName']:<50} {module['moduleId']:<10}")

    print()


# print rozvrhu v tabulce
def print_timetable(timetable):
    week_array = [None] * 5
    dny = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]
    for indx, day in enumerate(timetable):
        day_array = [""] * 9
        day_array[0] = dny[indx]
        for lesson in day:
            lesson_text = f"{lesson.subject_abbrev}\n{lesson.classroom_abbrev}\n{lesson.teacher_abbr}"
            # print(lesson.lesson_from, lesson.lesson_to)
            day_array[int(lesson.lesson_from)] = lesson_text
            day_array[int(lesson.lesson_to)] = lesson_text

        week_array[indx] = day_array

    week_array.insert(0, ["", "1", "2", "3", "4", "5", "6", "7", "8"])

    print(tabulate(week_array, tablefmt="fancy_grid"))


# print absencí v tabulce
def print_absences(absences, absences_in_subject, summary):

    day_array = [
        [
            "datum",
            "omluveno",
            "neomluveno",
            "nezapočítáno",
            "nevyhodnoceno",
            "nevyhodnoceno_s_omluvou",
        ]
    ]
    for date, day in absences.items():
        date = datetime.datetime.strptime(day.date.split("T")[0], "%Y-%m-%d")
        day_array.append(
            [
                date.strftime("%m-%d-%Y"),
                day.excused,
                day.unexcused,
                day.notcounted,
                day.unevaluated,
                day.unevaluated_with_apology,
            ]
        )

    print(tabulate(day_array, tablefmt="fancy_grid"))

    subject_array = [
        [
            "předmět",
            "absence",
            "procenta",
            "počet hodin",
            "omluveno",
            "neomluveno",
            "nezapočítáno",
            # "nevyhodnoceno",
            # "nevyhodnoceno_s_omluvou",
            "povolené absence",
            "povolené procenta",
        ]
    ]
    for (
        subject_name,
        absences_instance,
    ) in absences_in_subject.items():  # Iterate over items
        subject_array.append(
            [
                subject_name,  # Use the key directly
                absences_instance.absences,
                absences_instance.number_of_hours,
                absences_instance.excused,
                absences_instance.unexcused,
                absences_instance.notcounted,
                # absences_instance.unevaluated,
                # absences_instance.unevaluated_with_apology,
            ]
        )
    print(tabulate(subject_array, tablefmt="fancy_grid"))

    summary_array = [
        [
            "absence",
            "počet hodin",
            "omluveno",
            "neomluveno",
            "nezapočítáno",
            "nevyhodnoceno",
            "nevyhodnoceno_s_omluvou",
        ],
    ]
    summary_array.append(
        [
            summary.absences,
            summary.hours,
            summary.excused,
            summary.unexcused,
            summary.notcounted,
            summary.unevaluated,
            summary.unevaluated_with_apology,
        ]
    )

    print(tabulate(summary_array, tablefmt="fancy_grid"))


# print známek v tabulce s fancy názvy předmětů


def print_marks(marks_in_subject):
    for subject in marks_in_subject:
        print(pyfiglet.figlet_format(subject.subject_name, width=180))
        print("Průměr: ", subject.marks_avg, "\n")
        mark_array = []
        for indx, mark in enumerate(subject.marks):
            mark_date = datetime.datetime.strptime(
                mark.mark_date.split("T")[0], "%Y-%m-%d"
            )  # Convert mark_date to datetime object
            arr = [
                indx,
                mark_date.strftime("%m-%d"),  # Use mark_date instead of mark.mark_date
                mark.theme,
                mark.mark_value,
                mark.weight,
                mark.class_average,
            ]
            mark_array.append(arr)
        print(tabulate(mark_array, tablefmt="fancy_grid"))


def print_messages(messages):
    prnt = [["", "send_date", "sender", "title"]]
    for indx, message in enumerate(messages):
        prnt.append([indx, message.send_date, message.sender, message.title])

    print(tabulate(prnt, tablefmt="fancy_grid"))


def print_one_message(user, indx):
    message = messages.message_parser(messages.get_messages_download(user))[indx]
    print(f"From: {message.sender}")
    print(f"Date: {message.send_date}")
    print(f"Title: {message.title}")
    soup = BeautifulSoup(message.text, "html.parser")
    text = soup.get_text()
    print(f"Text: {text}")


# def main():
# import marks
# import user_handler
# import requests
# import pyfiglet

# user = user_handler.User()
# user.get_data()

# print_absences(absences.absences_parser(absences.get_absences_download(user)))
# user =
# print_timetable(timetable.timetable_week_parser(timetable.get_timetable(user)))
# # timetabl = timetable.timetable_week_parser(open('timetable_response.json', 'r').read())
# print_timetable(timetabl)


if __name__ == "__main__":
    pass
