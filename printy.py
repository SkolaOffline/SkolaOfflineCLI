from tabulate import tabulate
import pyfiglet
import datetime

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
        day_array = [""] * 10
        day_array[0] = dny[indx]
        for lesson in day:
            lesson_text = f"{lesson.subject_abbrev}\n{lesson.classroom_abbrev}\n{lesson.teacher_abbr}"
            # print(lesson.lesson_from, lesson.lesson_to)
            day_array[int(lesson.lesson_from)] = lesson_text
            day_array[int(lesson.lesson_to)] = lesson_text

        week_array[indx] = day_array

    print(tabulate(week_array, tablefmt="fancy_grid"))


# print absencí v tabulce
def print_absences(absences):
    day_array = []
    for date, day in absences.items():
        day_array.append(
            [
                date,
                day.excused,
                day.unexcused,
                day.notcounted,
                day.unevaluated,
                day.unevaluated_with_apology,
            ]
        )

    print(tabulate(day_array, tablefmt="fancy_grid"))


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
    for message in messages:
        print(
            message.send_date,
            "|",
            "Odesílatel:",
            message.sender,
            "|",
            "Zpráva:",
            message.title,
            "|",
            message.text,
            "|",
            "Přílohy:",
            message.attachments,
            "\n",
            "----------------------------------------------------------------------------------------------",
            "\n",
        )
    print()


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
