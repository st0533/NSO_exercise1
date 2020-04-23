from flask import Flask
from flask_cors import CORS
from flask import request
import  json

from data import listOfApplication

app = Flask('server')
CORS(app)
@app.route('/GET',methods=["GET"])
def get():
    return "hello world"


@app.route('/AddMessage', methods=["POST"])
def addMessage():
    data=request.args
    for a in listOfApplication:
        if a.applicationId == data['application_id']:
            for s in a.listOfSession:
                if s.sessionId == data['session_id']:
                    s.addMessage(data['message_id'],data['content'],data['participants'])

@app.route('/GetMessage/',methods=["get"])
def getMessageByApp():
    res=[]
    applicationId=1#request.form.get('applicationId')
    for a in listOfApplication:
        if a.applicationId == applicationId:
            res= a.getMessages()

    return json.dumps(res)




if __name__ == '__main__':
    app.run(threaded=True)