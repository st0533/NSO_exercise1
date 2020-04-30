class Application():
    applicationCounter = 0

    def __init__(self, applicationId=None, listOfSession=None):
        if applicationId == None:
            Application.applicationCounter += 1
            self.applicationId = Application.applicationCounter
            self.listOfSession = []
        else:
            self.applicationId = applicationId
            self.listOfSession = listOfSession  # list of session to this app

    def removeMessages(self):
        for s in self.listOfSession:
            s.listOfMessage = []  # remove all messages from all sessions

    def addSession(self, session):  # create new session
        self.listOfSession.append(session)

    def getMessages(self):
        newlist = []
        for s in self.listOfSession:
            newlist.append(s.getMessages())
        return newlist

    def getSession(self):
        newlist = []
        for s in self.listOfSession:
            dictTemp = {'sessionId': s.sessionId, 'messages': s.getMessages()}
            newlist.append(dictTemp)
            dictTemp = {}

        return newlist
