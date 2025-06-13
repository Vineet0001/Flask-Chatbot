from flask import Flask, render_template, request
from flask_cors import CORS
from bot_logic import get_bot_response

app = Flask(__name__)
CORS(app)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_message = request.form["message"]
        bot_message = get_bot_response(user_message)
        chat_history.append({"user": user_message, "bot": bot_message})
    return render_template("index.html", messages=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
