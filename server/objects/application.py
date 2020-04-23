from objects.session import Session
from data import *

class Application:
    applicationCounter = 0

    def __init__(self):
        Application.applicationCounter += 1
        self.applicationId = Application.applicationCounter
        self.listOfSession = []  # list of session to this app


    def removeAllMessages(self):
        for s in self.listOfSession:
            s.listOfMessage = []  # remove all messages from all sessions

    def addSession(self,session):  #create new session
        self.listOfSession.append(session)
    def getMessages(self):
        messages={}
        counter=0
        for s in self.listOfSession:
            messages[counter]=s.listOfMessage
            counter+=1
        return messages

