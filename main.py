
import flask
import random
from flask import render_template
from flask import request

app = flask.Flask(__name__)
codes = []
players = ['highonmelatonin','highongelato','lowondopamine','highoncortisol']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lobby', methods = ['POST'])
def lobby():
    player = request.form.get("player")
    code = random.randint(10000,99999)
    codes.append([code,[]])
    return render_template('lobby.html', code = code, players = players)


@app.route('/join/<code>', methods = ['POST'])
def join():
    return render_template('player.html')


@app.route('/setup/<code>', methods = ['POST'])
def setup(code):
    code = request.form.get("code")
    number = request.form.get("number")
    number = int(number)
    return render_template('setup.html', players = players, number = number)


@app.route('/game/', methods = ['POST'])
def game():
    selected = request.form.get("selected")
    code = request.form.get("code")
    print(selected)
    print(players)
    return render_template('game.html', players = players)


if __name__ == '__main__':
    app.run(debug = True)

