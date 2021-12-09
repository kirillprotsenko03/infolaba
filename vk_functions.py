import random
import vk
from encoding import ders_crypt, decoding


def send_vk_message(data: dict, token: str):
    if data["type"] == "message_new":
        session = vk.Session(access_token=token)
        api = vk.API(session, v=5.95)
        user_id = data["object"]["from_id"]
        text = data["object"]["text"]
        text = text.split()
        command = text[0]
        text = text[1:]
        message = ""
        for word in text:
            message += word
        if command == "закодируй":
            message += ders_crypt(text)

        if command == "раскодируй":
            message += decoding(text)

        api.messages.send(user_ids=user_id, message=message,
                          access_token=token, random_id=random.randint(-2147483648, 2147483647))
