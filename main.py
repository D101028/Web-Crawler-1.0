from statistics import mode
from flask import Flask, render_template, make_response, request, url_for
from function import function as f
import json
with open("./setting/setting.json", mode="rb") as file:
    set_data=json.loads(file.read())

app=Flask(__name__, static_folder="files")

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/signal/", methods=["GET"])
def home01():
    return render_template("home.html")

@app.route("/signal/<signal>", methods=['GET'])
def signal_(signal):
    try:
        if request.cookies.get("signal") == set_data['signal']:
            return render_template("main.html", right_signal=True)
    except:
        pass
    if signal!=set_data["signal"]:
        return render_template("redirect_to_home.html")
    else:
        resp = make_response(render_template("main.html", right_signal=True))
        resp.set_cookie(key="signal", value=signal, expires=None)
        return resp

# @app.route("/set")
# def setcookie(signal):
#     resp = make_response(render_template("main.html", right_signal=True))
#     resp.set_cookie(key="signal", value=signal)
#     return resp


@app.route("/download/", methods=["GET"])
def download_page():
    try:
        if request.cookies.get("signal") == set_data['signal']:
            return render_template("download.html")
        else:
            return render_template('wrong.html')
    except:
        return render_template('wrong.html')


@app.route("/error", methods=["GET"])
def error():
    return render_template("wrong.html")

# @app.route("/download/<data>", methods=["GET"])
# def redirect(data=None):
#     return render_template("main.html", data=data)

if __name__=="__main__":
    app.run(debug=True)
