from flask import Flask, render_template
from os import getcwd

print(getcwd())

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("gps.html")

@app.route("/favicon.ico")
def favicon():
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)