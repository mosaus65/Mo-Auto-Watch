import json
from flask import Flask, render_template

app = Flask(__name__)

def load_profile():
    with open("links.json", "r") as file:
        return json.load(file)

@app.route("/")
def home():
    profile_data = load_profile()
    return render_template("index.html", profile=profile_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)