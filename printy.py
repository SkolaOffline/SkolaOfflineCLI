from tabulate import tabulate
import pyfiglet
import datetime


def print_modules(modules):
    for x, module in enumerate(modules):
        module = module["module"]
        print(f"{x}: {module['moduleId']:<10}")
        # print(f"{x}: {module['moduleName']:<50} {module['moduleId']:<10}")

    print()


def print_timetable(timetable):
    week_array = [None] * 5
    dny = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]
    for indx, day in enumerate(timetable):
        day_array = [""] * 10
        day_array[0] = dny[indx]
        for lesson in day:
            lesson_text = f"{lesson.subject_abbrev}\n{lesson.classroom_abbrev}\n{lesson.teacher_abbr}"
            print(lesson.lesson_from, lesson.lesson_to)
            day_array[int(lesson.lesson_from)] = lesson_text
            day_array[int(lesson.lesson_to)] = lesson_text

        week_array[indx] = day_array

    print(tabulate(week_array, tablefmt="fancy_grid"))


def print_marks(marks_in_subject):
   for subject in marks_in_subject:
        print(pyfiglet.figlet_format(subject.subject_name, width=180))
        mark_array = []
        for indx, mark in enumerate(subject.marks):
            mark_date = datetime.datetime.strptime(mark.mark_date.split("T")[0], "%Y-%m-%d")  # Convert mark_date to datetime object
            arr = [
                indx,
                mark_date.strftime("%m-%d"),  # Use mark_date instead of mark.mark_date
                mark.theme,
                mark.mark_value,
                mark.weight,
                mark.class_average
            ]
            mark_array.append(arr)
        print(tabulate(mark_array, tablefmt='fancy_grid'))





def main():
    import marks
    import user_handler
    import requests
    import pyfiglet

    user = user_handler.User()
    user.get_data()

    print_marks(marks.all_marks_parser(marks.get_marks_download(user)))
    # user =
    # print_timetable(timetable.timetable_week_parser(timetable.get_timetable(user)))
    # # timetabl = timetable.timetable_week_parser(open('timetable_response.json', 'r').read())
    # print_timetable(timetabl)


if __name__ == "__main__":
    main()
