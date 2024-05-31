def print_modules(modules):
    for x, module in enumerate(modules):
        module = module['module']
        print(f"{x}: {module['moduleId']:<10}")
        # print(f"{x}: {module['moduleName']:<50} {module['moduleId']:<10}")

    print()
    

def print_timetable(timetable):
    for x in range(1, 9):
        print(f"{x:<15}", end='')
    print()

    # todo: fix this
    # it's just horrible
    for day in timetable:
        for lesson in day:
            jak_dlouho = int(lesson.lesson_to) - int(lesson.lesson_from) + 1
            print(lesson.subject_abbrev +\
                  '.'*(15*jak_dlouho-len(lesson.subject_abbrev)-5)+\
                  ' '*(5),
                  end='')

        print()
    





import timetable
def main():
    timetabl = timetable.timetable_week_parser(open('timetable_response.json', 'r').read())
    print_timetable(timetabl)

if __name__ == '__main__':
    main()