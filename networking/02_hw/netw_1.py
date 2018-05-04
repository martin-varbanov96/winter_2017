import socket

#destination host
host = 'localhost'
#destination port
port = 12345

#socket creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#let's use it as a client
s.connect((host, port))
s.send("Hi!")
s.close()
