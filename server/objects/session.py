class Session():
    sessionCounter = 0

    def __init__(self, sessionId=None, listOfMessages=None):
        if sessionId == None:
            Session.sessionCounter += 1
            self.sessionId = Session.sessionCounter
            self.listOfMessage = []
        else:
            self.sessionId = sessionId
            self.listOfMessage = listOfMessages

    def addMessage(self, message):  # add new message
        self.listOfMessage.append(message)

    def getMessages(self):
        return [m.getMessages() for m in self.listOfMessage]

    def removeMessages(self):
        self.listOfMessage = []
