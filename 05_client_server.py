import socket
import sys
from _thread import *

host = ''
port = 5555 # can use any port number

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	soc.bind((host, port))
except socket.error as e:
	print(str(e))

# size of connections can be handled
soc.listen(5)
print('Waiting for a connection....')
def threaded_client(connection):
	connection.send(str.encode('Welcome, to the first client server model\nType and press Enter to send\n'))

	while True:
		data = connection.recv(2048)
		reply = 'Server received: '+data.decode('utf-8')

		if not data:
			break
		connection.sendall(str.encode(reply))

	connection.close()


while True:
	connection, address = soc.accept()
	print(f'connected to: {address[0]} : {str(address[1])}')
	start_new_thread(threaded_client, (connection,))