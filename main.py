import logging.config
import logging
import user_handler
import printy
import argparse
import timetable
import marks
import absences
import messages
import report

parser = argparse.ArgumentParser(description="Skolni API")
# parser.add_argument("-l", "--login", action="store_true", help="runs the login process")
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
parser.add_argument(
    "-k",
    "--message",
    help="show a specific message by its index in --messages",
    action="store",
    type=int,
    default=None,
)
parser.add_argument(
    "-r",
    "--report",
    action="store_true",
    help="prints the report",
)
# parser.add_argument(
#     '-o',
#     '--logout',
#     action='store_true',
#     help='logs out the user'
# )


logging.basicConfig(level=logging.DEBUG)


def main(args):
    # if args.login:
    #     token_handler.token_login()
    #     return

    user = user_handler.User()
    user.get_data()

    # if args.logout:
    #     token_handler.token_logout()
    #     return

    if args.timetable:
        timetabl = timetable.get_timetable(user)
        printy.print_timetable(timetabl)
        # return

    if args.marks:
        marks_in_subject = marks.all_marks_parser(marks.get_marks_download(user))
        printy.print_marks(marks_in_subject)
        # return

    if args.absences:
        absence, absences_in_subject, summary = absences.absences_parser(
            absences.get_absences_download(user),
            absences.get_absences_in_subjects_download(user),
        )
        printy.print_absences(absence, absences_in_subject, summary)
        # return

    if args.messages:
        printy.print_messages(
            messages.message_parser(messages.get_messages_download(user))
        )
        # return

    if args.message:
        printy.print_one_message(user, args.message)
        # return

    if args.report:
        reports = report.report_parser(report.get_report_download(user))
        printy.print_report(reports)
        # return


if __name__ == "__main__":
    main(args=parser.parse_args())
