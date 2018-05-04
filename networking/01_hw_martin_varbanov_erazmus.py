import socket
from urllib.parse import quote_plus
import json

sock = socket.socket()
sock.connect(('maps.googleapis.com', 80))
geometry_index = 'geometry'
locating_index = 'location'
result_index = 'results'
request_text = """\
GET /maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH\r\n\
Host: maps.google.com:80\r\n\
User-Agent: search4.py (Foundations of Python Network Programming)\r\n\
Connection: close\r\n\
\r\n\
"""

request_text = request_text.format()
sock.sendall(request_text.encode('ascii'))
raw_reply = b''
while True:
    more = sock.recv(4096)
    if not more:
        break
    raw_reply += more
result_arr = json.loads(raw_reply.decode('utf-8'))
print(result_arr[result_index][0][geometry_index][locating_index])



# [0][geometry_index][locating_index] this has to be tried !!

# HTTP/1.1 ?! Shouldn't be HTTPS or the new google http ?

#working: GET /maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH\r\n

