import ast
import json
from server.objects.application import *
from server.objects.message import *
from server.objects.session import *

listOfApplication = []


def getMessage(messageId):
    for a in listOfApplication:
        for s in a:
            for m in s:
                if m.messageId == messageId:
                    return


def removeMessage(messageId):
    for a in listOfApplication:
        for s in a:
            for m in s:
                if m.messageId == messageId:
                    s.remove(m)
                    return


# applications:
app1 = Application()
app2 = Application()
listOfApplication.append(app1)
listOfApplication.append(app2)

# session:
ses1 = Session()
ses2 = Session()
ses3 = Session()
ses4 = Session()
ses5 = Session()
ses6 = Session()

app2.addSession(ses4)
app2.addSession(ses5)
app2.addSession(ses6)
app1.addSession(ses1)
app1.addSession(ses2)
app1.addSession(ses3)

# messages
mes1 = Message("aaa", "how are you?", ["david", "ron"])
mes2 = Message("bb", "fine", ["david", "ron"])
mes3 = Message("ccc", "what are you doing?", ["gad", "moshe"])
mes4 = Message("ddd", "all fine?", ["avi", "amit"])
mes5 = Message("eee", "are you OK?", ["noa", "rachel"])
mes6 = Message("fff", "thank you", ["sara", "lea"])
mes7 = Message("ggg", "please, help!", ["haddas", "lev"])
mes8 = Message("hhh", "s.o.s", ["gad", "moshe"])
mes9 = Message("iiii", "can you help me?", ["yaakov", "rachel"])
mes10 = Message("jjj", "i love you!", ["zeev", "chaim"])
mes11 = Message("kkk", "I will go", ["arie", "shani"])
mes12 = Message("lll", "dont forget me!!", [["david", "namma"]])
mes13 = Message("mmm", "do you want that?", ["refael", "dov"])
mes14 = Message("nnn", "listen to me", ["avi", "amit"])
mes15 = Message("ooo", "are you finish?", ["noa", "rachel"])

ses1.addMessage(mes1)
ses1.addMessage(mes2)
ses1.addMessage(mes3)

ses2.addMessage(mes4)
ses2.addMessage(mes5)
ses2.addMessage(mes6)

ses3.addMessage(mes7)
ses3.addMessage(mes8)

ses4.addMessage(mes9)
ses4.addMessage(mes10)
ses4.addMessage(mes11)

ses5.addMessage(mes12)
ses5.addMessage(mes13)

ses6.addMessage(mes14)
ses6.addMessage(mes15)
dict = {}
# create json file
with open('data.json', 'w') as outfile:
    appl = {}
    listOfApplicationToJson = []
    for i in listOfApplication:
        # tryd=i.getMessages()
        dict['applicationId'] = i.applicationId
        dict['listOfSession'] = i.getSession()
        listOfApplicationToJson.append(dict)
    appl['listOfApplication'] = listOfApplicationToJson
    json.dump(appl, outfile)
