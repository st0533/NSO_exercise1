from objects.message import *
from data import *


class Session:
    sessionCounter = 0

    def __init__(self):
        Session.sessionCounter += 1
        self.sessionId = Session.sessionCounter
        self.listOfMessage = []

    def addMessage(self,message):  # add new message
        self.listOfMessage.append(message)

    def getMessages(self):
        return self.listOfMessage

    def removeMessages(self):
        self.listOfMessage = []
