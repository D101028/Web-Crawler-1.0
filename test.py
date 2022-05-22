from flask import Flask, render_template, url_for
from function import function as f
import json
with open("./setting/setting.json", mode="rb") as file:
    set_data=json.loads(file.read())

app=Flask(__name__, static_folder="ico")

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/signal/<signal>", methods=['GET'])
def signal_(signal):
    if signal!=set_data["signal"]:
        return render_template("redirect_to_home.html")
    else:
        return render_template("main.html", right_signal=True)
    


@app.route("/error", methods=["GET"])
def error():
    return render_template("wrong.html")

@app.route("/download/<data>", methods=["GET"])
def redirect(data=None):
    return render_template("main.html", data=data)

if __name__=="__main__":
    app.run(debug=True)
