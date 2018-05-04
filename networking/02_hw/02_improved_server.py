import socket

#on every ip of this host
host = '192.168.0.10'
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

x = -9999
y = -9999
address_dict = dict()

while True:
	#UDP receive data:
	reposnce_server, address = s.recvfrom(BYTES)
	working_responce = reposnce_server.decode('ascii')
	address_dict[address] = working_responce
	return_value = "0 0"
	for el in address_dict:
		return_value = address_dict[el] + "|" + return_value
	return_value=return_value.encode('ascii')
	for addr_key in address_dict:
		s.sendto(return_value,addr_key)
