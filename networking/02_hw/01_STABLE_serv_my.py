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
#--==Question==-- Can I seek for explanation
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#making this socket a server
s.bind(FULL_ADDRESS)

while True:
	#UDP way:
	data, address = s.recvfrom(BYTES)
	#Send response
	s.sendto(data,address)
