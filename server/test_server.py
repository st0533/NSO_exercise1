import requests
def test_GetMessage_by_applicationId():
    response = requests.get("http://127.0.0.1:5000/GetMessage?applicationId=1")
    assert response.status_code == 200
def test_GetMessage_by_sessionId():
    response = requests.get("http://127.0.0.1:5000/GetMessage?sessionId=3")
    assert response.status_code == 200
def test_GetMessage_by_messagId():
    response = requests.get("http://127.0.0.1:5000/GetMessage?messageId=aaa")
    assert response.status_code == 200


def test_DeleteMessage_by_applicationId():
    response = requests.get("http://127.0.0.1:5000/DeleteMessage?applicationId=1")
    assert response.status_code == 200
def test_DeleteMessage_by_sessionId():
    response = requests.get("http://127.0.0.1:5000/DeleteMessage?sessionId=3")
    assert response.status_code == 200
def test_DeleteMessage_by_messagId():
    response = requests.get("http://127.0.0.1:5000/DeleteMessage?messageId=iiii")
    assert response.status_code == 200
def test_AddMessage():
    response = requests.get("http://127.0.0.1:5000/AddMessage?data={'application_id': 1, 'session_id':2, 'message_id': 'hmmmmmmm', 'participants': ['I','you'] , 'content':'opppp'}")
    assert response.status_code == 200
