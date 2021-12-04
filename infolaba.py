import os
import random
from flask import Flask, request
import vk


TOKEN = "e66acb2b35eefc2a12e3ff3dbd9e259be3a15e1909da70b6dcb1383508a429e3e550e2ceff94e395a31de"
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def message_handle():
    if request.method == "POST":
        data = request.get_json()
        if data["type"] == "message_new":
            session = vk.Session(access_token=TOKEN)
            api = vk.API(session, v=5.95)
            user_id = data["object"]["from_id"]
            api.messages.send(user_ids=user_id, message="я буду работать когда саня скинет код библиотеки", access_token=TOKEN,
                              random_id=random.randint(-2147483648, 2147483647))
            return "ok", 200
    else:
        return "hello, world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
