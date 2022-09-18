import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


def randomize(color_list):
    new_list=[]
    for i in range(5):
        new_list.append(color_list.pop(random.randint(0,len(color_list)-1)))
    return new_list

@app.route("/")
def main_page():
    return render_template('home.html')


@app.route("/shoe", methods=["POST"])
def shoe():
    color1 = request.form.get("color1")
    color2 = request.form.get("color2")
    color3 = request.form.get("color3")
    color4 = request.form.get("color4")
    color5 = request.form.get("color5")
    color_list = [color1,color2,color3,color4,color5]
    shuffled = randomize(color_list)
    return render_template("home2.html", color1=shuffled[0], color2=shuffled[1], color3=shuffled[2], color4=shuffled[3],
                           color5=shuffled[4])
