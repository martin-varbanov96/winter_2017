import socket
sock = socket.socket()
sock.connect(('maps.googleapis.com', 80))
var_sample = """\
GET /maps/api/geocode/json?address=207 N. Defiance St, Archbold, OH&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: search4.py\r\n\
Connection: close\r\n\
\r\n\
"""
var_mine ="""
    'GET /maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH'
    '&sensor=false HTTP/1.1\r\n'
    'Host:maps.google.com:80\r\n'
    'User-Agent: search4.py\r\n'
    'Connection: close\r\n'
    '\r\n'
"""


    #request = request_text.format(quote_plus(address))
    #print(request)
    #sock.sendall(request.encode('ascii'))
    #raw_reply = b''
    
sock.sendall(var_sample.encode('ascii'))
raw_reply = b''
while True:
    more = sock.recv(4096)
    if not more:
        break
    raw_reply += more
print(raw_reply)


#1600+Amphitheatre+Parkway,+Mountain+View,+CA&key

# HTTP/1.1 ?! Shouldn't be HTTPS or the new google http ?

