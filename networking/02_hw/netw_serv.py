#import socket
import socket
#on every ip of this host
host = ''
#on this port no
port = 12345

#socket creation
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to get rid of "socket already in use" while restarting the server
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#making this socket a server
s.bind((host, port))
#starting to listen
s.listen(1)

print("I'm listening")

while True:
    #answering a call
    conn, addr = s.accept()
    print("Got a connection from:", addr)
    #get no more than 1k of data
    data = conn.recv(1024)
    if data:
        data_string = data.encode('utf-8')
        print(data_string)
        #hanging up
        conn.close()
