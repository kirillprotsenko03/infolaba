import os
from flask import Flask, request
from vk_functions import send_vk_message


TOKEN = "e66acb2b35eefc2a12e3ff3dbd9e259be3a15e1909da70b6dcb1383508a429e3e550e2ceff94e395a31de"
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def message_handle():
    if request.method == "POST":
        data = request.get_json()
        send_vk_message(data, TOKEN)
        return "ok", 200
    else:
        return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
