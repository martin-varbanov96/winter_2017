import socket

host = ''
port = 12345
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setblocking(0)
s.bind((host,port))
s.listen(1)
print("I'm listening")
while True:
	conn, addr = s.accept()
	print("Connecting from {}".format(addr))

	data = conn.recv(1024)
	if data:
		#data_string = data.encode('utf-8')
		print(data)
		print(type(data))
		conn.close()
