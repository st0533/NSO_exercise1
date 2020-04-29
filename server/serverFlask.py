from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import json
import ast

from server.data import *

app = Flask('serverF')
CORS(app)


@app.route('/GET', methods=["GET"])
def get():
    return "hello world"


@app.route('/AddMessage', methods=["GET","POST"])
def addMessage():
    data = ast.literal_eval(request.args.get('data'))
    for a in listOfApplication:
        if a.applicationId == int(data['application_id']):
            for s in a.listOfSession:
                if s.sessionId == data['session_id']:
                    m=Message(data['message_id'], data['content'], data['participants'])
                    s.addMessage(m)
                    return "added"
    return "opssssssss"


@app.route('/GetMessage', methods=["get"])
def getMessage():
    applicationId = request.args.get('applicationId')
    sessionId=request.args.get('sessionId')
    messageId=request.args.get('messageId')
    if applicationId:
        applicationId=int(applicationId)
        for a in listOfApplication:
            if a.applicationId == applicationId:
                return json.dumps(a.getMessages())
    if sessionId:
        sessionId=int(sessionId)
        for a in listOfApplication:
            for s in a.listOfSession:
                if s.sessionId==sessionId:
                    return json.dumps(s.getMessages())
    if messageId:
        for a in listOfApplication:
            for s in a.listOfSession:
                for m in s.listOfMessage:
                    if m.messageId==messageId:
                        return json.dumps(m.getMessages())


@app.route('/DeleteMessage', methods=["get"])
def deleteMessage():
    applicationId = request.args.get('applicationId')
    sessionId=request.args.get('sessionId')
    messageId=request.args.get('messageId')
    if applicationId:
        applicationId=int(applicationId)
        for a in listOfApplication:
            if a.applicationId == applicationId:
                a.removeMessages()
                return "seccsess"
    if sessionId:
        sessionId=int(sessionId)
        for a in listOfApplication:
            for s in a.listOfSession:
                if s.sessionId==sessionId:
                    s.removeMessages()
                    return "seccsess"
    if messageId:
        for a in listOfApplication:
            for s in a.listOfSession:
                for m in s.listOfMessage:
                    if m.mlessageId==messageId:
                        s.listOfMessage.remove(m)
                        return "seccsess"

if __name__ == '__main__':
    app.run(threaded=True)
