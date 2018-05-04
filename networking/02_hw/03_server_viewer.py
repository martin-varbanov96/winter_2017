import socket

#on every ip of this host
host = ''
#on this port no
port = 12345

#limit of Bytes:
BYTES = 1024

FULL_ADDRESS = (host, port)

#socket creation
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#to get rid of "socket already in use" while restarting the server
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#making this socket a server
s.bind(FULL_ADDRESS)
#starting to listen
#s.listen(1)

print("I'm listening")

data = bytes()
addr_arr = list()

while True:
    #answering a call
    #FOR TCP conn, addr = s.accept()
    #print("Got a connection from:", addr)
    
    #get no more than 1k of data
    #data = conn.recv(1024)
    
    #UDP receive data:

	data, address = s.recvfrom(BYTES)
	working_data_var = data.decode('ascii')
	if(working_data_var == "viewer"):
		addr_arr.append(address)
		s.sendto(b'0 0',address)		

	s.sendto(data,address)