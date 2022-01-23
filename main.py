import flask
import random
import socket
#import tqdm
import os
from flask import render_template,url_for,request

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

app = flask.Flask(__name__)
HOST = '127.0.0.1'
PORT = random.randint(1024,49151)

filename = "home.html"
#filesize = os.path.getsize(filename)

##s = socket.socket()
##addr = (HOST,PORT)
##
##s.bind(addr)
##s.listen(5)
##
##while True:
##    c,(c_h,c_p) = s.accept()
##    c.send(f"{filename}{SEPARATOR}{filesize}".encode())

@app.route('/')
def home():
    return render_template('home.html') #Create game -> redirect to lobby

@app.route('/lobby.html',methods = ["GET","POST"])
def lobby():
    code = random.randint(0,1023) #port number
    if request.method == "GET":
        return render_template('lobby.html',code= PORT)
    if 'number' in request.form:
        number = request.form['number']
        return render_template("setup.html")
    

    


if __name__ == "__main__":
    app.run()
