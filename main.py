import token_handler
import user_handler
import printy
import argparse
import timetable
import marks
import absences
import messages


# Parser argumentů, pro help main.py -h
parser = argparse.ArgumentParser(description="Skolni API")
parser.add_argument("-l", "--login", action="store_true", help="runs the login process")
parser.add_argument(
    "-r",
    "--refreshlogin",
    action="store_true",
    help="tries to run the login process using stored refresh token",
)
parser.add_argument(
    "-t", "--timetable", action="store_true", help="prints the timetable"
)
parser.add_argument(
    "-m",
    "--marks",
    action="store_true",
    help="prints the marks",
)
parser.add_argument(
    "-a",
    "--absences",
    action="store_true",
    help="prints the absences",
)
parser.add_argument(
    "-z",
    "--messages",
    action="store_true",
    help="prints the messages",
)


# hlavní funkce, která zpracovává argumenty
def main(args):
    if args.login:
        token_handler.token_login()
        return

    if args.refreshlogin:
        token_handler.refresh_login()
        return

    # získání dat uživatele, provede se vždy
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

    if args.absences:
        absence = absences.absences_parser(absences.get_absences_download(user))
        printy.print_absences(absence)
        return

    if args.messages:
        message = messages.message_parser(messages.get_messages_download(user))
        printy.print_messages(message)
        return


if __name__ == "__main__":
    main(args=parser.parse_args())
