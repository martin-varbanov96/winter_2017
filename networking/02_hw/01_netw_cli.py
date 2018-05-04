import socket

#destination host
host = ''
#destination port
port = 12345

#socket creation
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#let's use it as a client
#MUST be string to get encode
num = 'asddsa'
bit_data = num.encode('ascii')
s.sendto(bit_data, (host, port))
counter = 0
while counter<100:
	s.sendto(bit_data, (host, port))
	counter+=0.7
s.close()