from flask import Flask, render_template, request, redirect, url_for
import webbrowser

from logic.enroll import enroll_user
from logic.train import train_model
from logic.recognize import recognize_user

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/enroll", methods=["POST"])
def enroll():
    user_id = request.form["user_id"]
    enroll_user(user_id)
    return redirect(url_for("home"))



@app.route("/train")
def train():
    train_model()
    return redirect(url_for("home"))


@app.route("/recognize")
def recognize():
    recognize_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
