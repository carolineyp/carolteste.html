from flask import Flask

app = Flask(__name__)


@app.route("/")
def olamundo():
    return "ola mundo"

@app.route("/sobre")
def sobre():
    return "<b>psr<b>"

app.run(debug=True)