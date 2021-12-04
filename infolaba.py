import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def message_handle():
    if request.method == "POST":
        data = request.get_json()
        if data["type"] == "confirmation" and data["group_id"] == 186539292:
            return "51457a67"
    else:
        return "hello, world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
