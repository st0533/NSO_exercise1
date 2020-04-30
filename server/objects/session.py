from server.objects.objectInterface import IInterface


class Session(IInterface):
    sessionCounter = 0
    def __init__(self,sessionId=None,listOfMessage=[]):
        if sessionId==None:
            Session.sessionCounter += 1
            self.sessionId = Session.sessionCounter
        else:
            self.sessionId=sessionId
        self.listOfMessage = listOfMessage

    def addMessage(self,message):  # add new message
        self.listOfMessage.append(message)

    def getMessages(self):
        messages=""
        for m in self.listOfMessage:
            messages+=str(m.getMessages())+","
        return messages[0:-1]

    def removeMessages(self):
        self.listOfMessage = []
