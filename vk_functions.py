import random
import vk
from encoding import ders_crypt, decoding
from requests.exceptions import ConnectionError


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

        message = message[:-1]
        if command.lower() == "закодируй":
            message = ders_crypt(message)
        elif command.lower() == "раскодируй":
            message = decoding(message)
        else:
            message = """Привет, ты наверное пользуешься ботом впервые или забыл как это делать.
Если тебе нужно закодировать сообщение, то напиши боту закодируй и свое сообщение.
Пример: закодируй привет.
Если тебе нужно раскодировать сообщение, то напиши боту раскодируй и свой код.
Например: раскодируй 112.1245.64.13"""

        api.messages.send(user_ids=user_id, message=message,
                          access_token=token, random_id=random.randint(-2147483648, 2147483647))


def send_game_vk_message(user_id: int, text: str, token: str):
    session = vk.Session(access_token=token)
    api = vk.API(session, v=5.95)
    try:
        api.messages.send(user_ids=user_id, message=text, access_token=token,
                          random_id=random.randint(-2147483648, 2147483647))
    except ConnectionError:
        print("sorry, you cant send message because you have not got internet connection yet")
