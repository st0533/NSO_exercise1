import ast
import json

from flask import Flask
from flask import request
from flask_cors import CORS

from server.objects.application import *
from server.objects.message import *
from server.objects.session import *

app = Flask('serverF')
CORS(app)


def convertData():
    db = {}
    with open('data.json', 'r') as outfile:
        db = json.load(outfile)
    listOfApplication = db['listOfApplication']
    res = []
    for a in listOfApplication:
        sessions = []
        for s in a["listOfSession"]:
            messages = []
            for m in s["messages"]:
                messages.append(Message(m["messageId"], m["content"], m["participants"]))
            sessions.append(Session(s["sessionId"], messages))
        res.append(Application(a["applicationId"], sessions))
    return res


listOfApplication = convertData()


def updateData():
    dict = {}
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


@app.route('/AddMessage', methods=["GET", "POST"])
def addMessage():
    data = ast.literal_eval(request.args.get('data'))
    for a in listOfApplication:
        if a.applicationId == int(data['application_id']):
            for s in a.listOfSession:
                if int(s.sessionId) == data['session_id']:
                    m = Message(data['message_id'], data['content'], data['participants'])
                    s.listOfMessage.append(m)
                    updateData()
                    return "added"


@app.route('/GetMessage', methods=["get"])
def getMessage():
    applicationId = request.args.get('applicationId')
    sessionId = request.args.get('sessionId')
    messageId = request.args.get('messageId')
    if applicationId:
        applicationId = int(applicationId)
        for a in listOfApplication:
            if a.applicationId == applicationId:
                return str(a.getMessages())
    if sessionId:
        sessionId = int(sessionId)
        for a in listOfApplication:
            for s in a.listOfSession:
                if s.sessionId == str(sessionId):
                    return json.dumps(s.getMessages())
    if messageId:
        for a in listOfApplication:
            for s in a.listOfSession:
                for m in s.listOfMessage:
                    if m.messageId == str(messageId):
                        return json.dumps(m.getMessages())



@app.route('/DeleteMessage', methods=["get"])
def deleteMessage():
    applicationId = request.args.get('applicationId')
    sessionId = request.args.get('sessionId')
    messageId = request.args.get('messageId')
    if applicationId:
        applicationId = int(applicationId)
        for a in listOfApplication:
            if a.applicationId == applicationId:
                a.removeMessages()
                updateData()
                return "seccsess"
    if sessionId:
        for a in listOfApplication:
            for s in a.listOfSession:
                if s.sessionId == sessionId:
                    s.removeMessages()
                    updateData()
                    return "seccsess"
    if messageId:
        for a in listOfApplication:
            for s in a.listOfSession:
                for m in s.listOfMessage:
                    if m.messageId == messageId:
                        s.listOfMessage.remove(m)
                        updateData()
                        return "seccsess"


if __name__ == '__main__':
    app.run(threaded=True)
