##This script contains the objects for a single room and a group of rooms

class room:
    def __init__(self, code):
        self.players = []
        self.code = code
        self.questions = []

    def addplayer(self,player):
        self.players.append(player)

    def getcode(self):
        return self.code

    def getplayers(self):
        return self.players

    def addquestion(self,question):
        self.questions.append(question)

    def getquestions(self):
        return self.questions


class rooms:
    def __init__(self):
        self.rooms = []

    def addroom(self, code):
        self.rooms += [room(code)]

    def joinroom(self, code, player):
        for i in range(len(self.rooms)):
            if self.rooms[i].getcode() == code:
                self.rooms[i].addplayer(player)
                return True

        return False

    
    def addquestion(self, code, question):
        for i in range(len(self.rooms)):
            if self.rooms[i].getcode() == code:
                self.rooms[i].addquestion(question)
                return True

        return False


    def getquestions(self, code):
        for i in range(len(self.rooms)):
            if self.rooms[i].getcode() == code:
                return self.rooms[i].getquestions()

        return False

    def getplayers(self, code):
        for i in range(len(self.rooms)):
            if self.rooms[i].getcode() == code:
                return self.rooms[i].getplayers()

        return False

    



    
    