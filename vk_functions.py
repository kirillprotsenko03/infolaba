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
        message = ""
        command = text[0]
        for word in text[1:]:
            message += word + " "
        if command == "закодируй":
            message = ders_crypt(message)
        elif command == "раскодируй":
            message = decoding(message)
        else:
            message = """привет, ты наверное пользуешься ботом впервые, или забыл как это делать.
                         если тебе нужно закодировать сообщение, то напиши боту закодируй и свое сообщение.
                         пример: закодируй привет.
                         если тебе нужно раскодировать сообщение, то напиши боту раскодируй и свой код.
                         например: раскодируй 112.1245.64.13"""

        api.messages.send(user_ids=user_id, message=message,
                          access_token=token, random_id=random.randint(-2147483648, 2147483647))
