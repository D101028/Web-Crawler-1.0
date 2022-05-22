from flask import Flask, render_template
import json
with open("./setting/setting.json", mode="rb") as file:
    set_data=json.loads(file.read())

# async def signal_judge(signal):
#     print(signal)
#     if signal!=set_data["signal"]:
#         return "window.location.href='/'"
#     else:
#         return render_template("main.html", right_signal=True)