from tabulate import tabulate

def print_modules(modules):
    for x, module in enumerate(modules):
        module = module['module']
        print(f"{x}: {module['moduleId']:<10}")
        # print(f"{x}: {module['moduleName']:<50} {module['moduleId']:<10}")

    print()
    

def print_timetable(timetable):
    week_array = [None]*5
    dny = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek']
    for indx, day in enumerate(timetable):
        day_array = ['']*10
        day_array[0] = dny[indx]
        for lesson in day:
            lesson_text = f'{lesson.subject_abbrev}\n{lesson.classroom_abbrev}\n{lesson.teacher_abbr}'
            print(lesson.lesson_from, lesson.lesson_to)
            day_array[int(lesson.lesson_from)] = lesson_text
            day_array[int(lesson.lesson_to)] = lesson_text

        week_array[indx] = day_array

    print(tabulate(week_array, tablefmt='fancy_grid'))





import timetable
def main():
    pass
    # user = 
    # print_timetable(timetable.timetable_week_parser(timetable.get_timetable(user))) 
    # # timetabl = timetable.timetable_week_parser(open('timetable_response.json', 'r').read())
    # print_timetable(timetabl)

if __name__ == '__main__':
    main()