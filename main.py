import requests
import token_handler
import json
import user_handler
import printy
import argparse
import timetable
import marks

parser = argparse.ArgumentParser(description="Skolni API")
parser.add_argument("-l", "--login", action="store_true", help="runs the login process")
parser.add_argument(
    "-t", "--timetable", action="store_true", help="prints the timetable"
)
parser.add_argument(
    "-m",
    "--marks",
    action="store_true",
    help="prints the marks",
)


def main(args):
    if args.login:
        token_handler.token_login()
        return

    user = user_handler.User()
    user.get_data()

    if args.timetable:
        timetabl = timetable.get_timetable(user)
        printy.print_timetable(timetabl)
        return

    if args.marks:
        marks_in_subject = marks.all_marks_parser(marks.get_marks_download(user))
        printy.print_marks(marks_in_subject)
        return


if __name__ == "__main__":
    main(args=parser.parse_args())
