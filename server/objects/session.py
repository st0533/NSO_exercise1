from server.objects import message
from server.data import *
import json
class Session:
    sessionCounter = 0
    def __init__(self):
        Session.sessionCounter += 1
        self.sessionId = Session.sessionCounter
        self.listOfMessage = []

    def addMessage(self,message):  # add new message
        self.listOfMessage.append(message)

    def getMessages(self):
        messages=""
        for m in self.listOfMessage:
            messages=messages+str(m.getMessages())
        return messages

    def removeMessages(self):
        self.listOfMessage = []
