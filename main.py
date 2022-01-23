import flask
import random
from flask import render_template
from flask import request

app = flask.Flask(__name__)
players = ['highonmelatonin', 'SomeNickname', 'GeneralKen0bi','lowondopamine','highoncortisol']

HOST = '127.0.0.1'
PORT = random.randint(

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lobby', methods = ['POST'])
def lobby():
    player = request.form.get("player")
    code = 8888
    return render_template('lobby.html', code = code, players = players)


@app.route('/join/', methods = ['POST'])
def join():
    return render_template('player.html')


@app.route('/setup/', methods = ['POST'])
def setup():
    number = request.form.get("number")
    number = int(number)
    number = 1
    return render_template('setup.html', players = players, number = number)


@app.route('/game/', methods = ['POST'])
def game():
    question = request.form.get("question")
    selected = request.form.get("selected")
    return render_template('game.html', players = players, question = question)


if __name__ == '__main__':
    app.run(debug = True)
