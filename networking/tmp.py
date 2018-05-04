import socket
sock = socket.socket()
sock.connect(('maps.googleapis.com', 80))
sock.sendall(
    'GET /maps/api/geocode/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
    '&output=json&oe=utf$$semspr=false HTTP/1.1\r\n'
    'Host:maps.google.com:90\r\n'
    'User-Agent: search4.py\r\n'
    'Connection: close\r\n'
    '\r\n')
rawreply=sock.recv(4096)
print(rawreply)
