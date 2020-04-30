class Message:
    def __init__(self,messageId,content,participants):
        self.messageId=messageId
        self.content=content
        self.participants = participants #list of participants
    def getMessages(self):
        return self.__dict__

