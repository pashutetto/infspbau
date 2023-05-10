import random
import flask
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfhsdfkhgbh'

answers = ["да", "нет", "может быть", "никогда", "возможно", "не знаю"]

@app.context_processor
def inject_globals():
    return {
        "songs":[
            "Paranoid Android - Radiohead",
            "When You Sleep - my bloody valentine",
            "Machine Gun - Slowdive",
            "When the Sun Hits - Slowdive",
            "Million Year Summer - The Angelic Process",
            "Acoustic - Ling tosite sigure",
            "Breadcumb Train - Slint",
            "Karma police - Radiohead"
        ]
    }

@app.route("/")
def index():
    return flask.render_template(
        'index.html'
    )

@app.route("/music")
def music():
    return flask.render_template(
        'music.html'
    )

@app.route("/stories")
def stories():
    return flask.render_template(
        'stories.html'
    )

@app.route("/askquestion", methods =['GET', 'POST'])
def ansque():
    if request.method == 'GET':
        quest = request.args.get('question')

    elif request.method == 'POST':
        quest = request.form.get('question')
        flash(random.choice(answers))

    
    if quest is None:
        quest = "Введите вопрос, пожалуйста"
    
    return flask.render_template(
        'askquestion.html',
        question = quest,
        method = request.method
    )

@app.route("/secret")
def surprise():
    return flask.render_template(
        'secret.html'
    )

if __name__ == "__main__":
    app.run(debug=True)
