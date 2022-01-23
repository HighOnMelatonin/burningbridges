from django.shortcuts import render
from scipy import rand
import helper
import flask
from flask import render_template
from flask import redirect
from flask import request
from random import randint


app = flask.Flask(__name__)

rooms = helper.rooms()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lobby', methods = ['POST'])
def createlobby():
    global rooms

    code = randint(1000,9999)
    code = 8888
    rooms.addroom(code)

    player = request.form.get("player")
    rooms.joinroom(code, player)

    print(rooms.getplayers(8888))
    return render_template('lobby.html', code = code)

print(rooms.getplayers(8888))

@app.route('/lobby/<code>', methods = ["POST"])
def lobby(code):
    if rooms.getplayers(code):
        players = rooms.getplayers(code)

    else:
        players = []
    
    print(players)
    
    return render_template('lobby.html', code = code, players = players)


@app.route('/join', methods = ["POST"])
def join(code):
    player = request.form.get("player")
    if rooms.joinroom(code, player):
        rooms.joinroom(code, player)
        return redirect(f"/lobby/{code}")

    else:
        message = "Invalid code"


@app.route('/question/<code>', methods = ["POST"])
def question(code):
    number = request.form.get("number")
    number = int(number)
    return render_template('setup.html', number = number, code = code)


@app.route('/game/<code>', methods = ["POST"])
def game(code):
    if rooms.getplayers(code):
        players = rooms.getplayers(code)

    else:
        players = ['There are no players']
    return render_template('game.html', players = players)


if __name__ == '__main__':
    app.run(debug = True)
