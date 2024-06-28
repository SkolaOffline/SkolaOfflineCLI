from dataclasses import dataclass
import requests
from datetime import datetime
import token_handler
import json
import time


# getter zpráv
def get_messages_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/messages/received",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        params={
            "dateFrom": formated_date(
                time.time() - 60 * 60 * 24 * 31
            ),  # 31 dní => zprávy za poslední měsíc
            "dateTo": formated_date(time.time()),
        },
    )
    # if unauthorized or bad credentials tries to get a new token from the refresh token
    if r.status_code == 401 or r.status_code == 400:
<<<<<<< HEAD
        token_handler.write_token_to_file_from_refresh_token()
=======
        token_handler.token_login()
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31
        r = requests.get(
            f"https://aplikace.skolaonline.cz/solapi/api/v1/messages/received",
            headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
            params={
                "dateFrom": formated_date(
                    time.time() - 60 * 60 * 24 * 31
                ),  # 31 dní => zprávy za poslední měsíc
                "dateTo": formated_date(time.time()),
            },
        )
        if r.status_code == 401 or r.status_code == 400:
<<<<<<< HEAD
            raise Exception("token expired")
=======
            raise Exception(
                "Something about your login went wrong. Check your credentials."
            )
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31

    # # print(r.text)
    # txt = r.text
    # txt = json.loads(txt)
    # for msg in txt['messages']:
    #     print(msg['title'])

    return r.text  # vrací json odpověd jako text (string)


# class pro zprávy
@dataclass
class Message:
    send_date = str
    read = bool
    sender = str
    attachments = list  # todo so it actually works
    title = str
    text = str
    message_id = str


# parsuje json zpráv
def message_parser(jsn):
    jsn = json.loads(jsn)["messages"]
    messages = []
    for message in jsn:
        messag = Message()
<<<<<<< HEAD
        messag.send_date = message["sentDate"]
=======
        # Parse the sentDate string into a datetime object assuming it's in ISO 8601 format
        sent_date_str = message["sentDate"]
        sent_date = datetime.strptime(
            sent_date_str, "%Y-%m-%dT%H:%M:%S.%f"
        )  # Adjust the format as necessary
        messag.send_date = sent_date.strftime("%m-%d-%Y")
>>>>>>> b1b2fb02c3478143bbf0960edede4b316d114e31
        messag.read = message["read"]
        messag.sender = message["sender"]["name"]
        messag.attachments = str(message["attachments"])
        messag.title = message["title"]
        messag.text = message["text"]
        messag.message_id = message["id"]
        messages.append(messag)

    return messages


# formátuje datum
def formated_date(date):
    date = float(date)
    return datetime.fromtimestamp(date).strftime("%Y-%m-%dT%H:%M:%S.000")


# tato funkce se spustí pokud spustíš messages.py

if __name__ == "__main__":
    # import requests
    # import token_handler
    # import json
    # import user_handler
    # import time
    # import datetime

    # user = user_handler.User()
    # user.get_data()

    # printy.print_messages(message_parser(get_messages_download(user)))¨
    pass
