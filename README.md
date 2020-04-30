my program implement messages prosses,
all application content list of sessions that  content list of messages
I used in JSON file to save data
(to build my data, I made data.py file (you can see it))
when my server starts to run it takes data from JSON file and work offline, (save time on actions that don't access to the database)

have 3 objects: application,session,messages

to run this program:
in cmd write: python [ADDRESS TO SERVERFLASK.PY]
copy the {host_ip}:{port}(example:127.0.0.1:5000) to browser
and add a method
you can see example in file test_server.py

the methods:
AddMessage
http://{host_ip}:{port}/AddMessage?data={"application_id": [APPLICATION_ID], "session_id":[SESSION_ID], "message_id": [MESSAGEID], "participants": [LIST_OF_PARTICIPANTS] , "content": [CONTENT] }

GetMessage:
http://{host_ip}:{port}/GetMessage?applicationId=[APPLICATION_ID]
http://{host_ip}:{port}/GetMessage?sessionId=[SESSION_ID]
http://{host_ip}:{port}/GetMessage?messageId=[MESSAGEID]

DeleteMessage:
http://{host_ip}:{port}/DeleteMessage?applicationId= [APPLICATION_ID]
http://{host_ip}:{port}/DelteMessage?sessionId=[SESSION_ID]
http://{host_ip}:{port}/DeleteMessage?messageId=[MESSAGEID]