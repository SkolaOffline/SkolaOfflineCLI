import requests
import token_handler
import json
import user_handler
import printy
import argparse
import timetable

parser = argparse.ArgumentParser(description='Skolni API')
parser.add_argument('--login', help='runs the login process')
parser.add_argument('--timetable', help='prints the timetable')



def main(args):
    if args.login:
        token_handler.token_login()
        return

    user = user_handler.User()
    user.get_data()

    if args.timetable:
        printy.print_timetable(timetable.get_timetable(user.personid))
        return
    


if __name__ == '__main__':
    main(args=parser.parse_args())