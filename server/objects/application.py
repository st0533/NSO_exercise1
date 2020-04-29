from server.data import *
import json
class Application:
    applicationCounter = 0

    def __init__(self):
        Application.applicationCounter += 1
        self.applicationId = Application.applicationCounter
        self.listOfSession = []  # list of session to this app


    def removeMessages(self):
        for s in self.listOfSession:
            s.listOfMessage = []  # remove all messages from all sessions

    def addSession(self,session):  #create new session
        self.listOfSession.append(session)
    def getMessages(self):
        messaegs=""
        for s in self.listOfSession:
            messaegs+=s.getMessages()
        return messaegs
