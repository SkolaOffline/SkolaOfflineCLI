from dataclasses import dataclass
import printy
import requests

#getter zpráv
def get_messages_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/messages/received",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        params={
            "dateFrom": formated_date(time.time() - 60 * 60 * 24 * 31), #31 dní => zprávy za poslední měsíc
            "dateTo": formated_date(time.time()),
        },
    )

    # # print(r.text)
    # txt = r.text
    # txt = json.loads(txt)
    # for msg in txt['messages']:
    #     print(msg['title'])

    return r.text #vrací json odpověd jako text (string)

#class pro zprávy
@dataclass
class Message:
    send_date = str
    read = bool
    sender = str
    attachments = list  # todo so it actually works
    title = str
    text = str
    message_id = str

#parsuje json zpráv
def message_parser(jsn):
    jsn = json.loads(jsn)["messages"]
    messages = []
    for message in jsn:
        messag = Message()
        messag.send_date = message["sentDate"]
        messag.read = message["read"]
        messag.sender = message["sender"]["name"]
        messag.attachments = str(message["attachments"])
        messag.title = message["title"]
        messag.text = message["text"]
        messag.message_id = message["id"]
        messages.append(messag)

    return messages

#formátuje datum
def formated_date(date):
    date = float(date)
    return datetime.datetime.fromtimestamp(date).strftime("%Y-%m-%dT%H:%M:%S.000")

#tato funkce se spustí pokud spustíš messages.py
#todo předělat do main.py
if __name__ == "__main__":
    import requests
    import token_handler
    import json
    import user_handler
    import time
    import datetime

    user = user_handler.User()
    user.get_data()

    printy.print_messages(message_parser(get_messages_download(user)))
