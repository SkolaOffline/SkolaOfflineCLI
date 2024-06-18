from dataclasses import dataclass

def get_messages_download(user):
    r = requests.get(
        f"https://aplikace.skolaonline.cz/solapi/api/v1/messages/received",
        headers={"Authorization": f"Bearer {token_handler.get_token_from_file()}"},
        params = {
            'dateFrom': formated_date(time.time()-60*60*24*31),
            'dateTo': formated_date(time.time())
        }
    )

    # # print(r.text)
    # txt = r.text
    # txt = json.loads(txt)
    # for msg in txt['messages']:
    #     print(msg['title'])

    return r.text


@dataclass
class Message():
    send_date = str
    read = bool
    sender = str
    attachments = list # todo so it actually works
    title = str
    text = str
    message_id = str



def message_parser(jsn):
    jsn = json.loads(jsn)['messages']
    messages = []
    for message in jsn:
        messag = Message()
        messag.send_date = message['sentDate']
        messag.read = message['read']
        messag.sender = message['sender']['name']
        messag.attachments = str(message['attachments'])
        messag.title = message['title']
        messag.text = message['text']
        messag.message_id = message['id']        
        messages.append(messag)

    return messages





def formated_date(date):
    date = float(date)
    return datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%dT%H:%M:%S.000')



if __name__ == '__main__':
    import requests
    import token_handler
    import json
    import user_handler
    import time
    import datetime

    user = user_handler.User()
    user.get_data()

    for mgs in message_parser(get_messages_download(user)):
        print(mgs.title)
