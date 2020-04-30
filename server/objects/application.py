from server.objects.objectInterface import IInterface


class Application(IInterface):
    applicationCounter = 0

    def __init__(self,applicationId=None,listOfSession=[]):
        if applicationId==None:
            Application.applicationCounter += 1
            self.applicationId = Application.applicationCounter
        else:
            self.applicationId=applicationId
        self.listOfSession = listOfSession  # list of session to this app


    def removeMessages(self):
        for s in self.listOfSession:
            s.listOfMessage = []  # remove all messages from all sessions

    def addSession(self,session):  #create new session
        self.listOfSession.append(session)
    def getMessages(self):
        messages=""
        for s in self.listOfSession:
            messages+=s.getMessages()+","
        return messages[0:-1]
    def getSession(self):
        messages = "["
        for s in self.listOfSession:
            messages += "{'sessionId':'" + str(s.sessionId) + "','messages':["
            messages += str(eval(s.getMessages())) + "]},"
        messages = messages[0:-1] + "]"
        return messages

