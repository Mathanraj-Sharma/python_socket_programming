import socket
import sys

host = ''
port = 5555 # can use any port number

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	soc.bind((host, port))
except socket.error as e:
	print(str(e))

# size of connections can be handled
soc.listen(5)

connection, address = soc.accept()

print(f'connected to: {address[0]} : {str(address[1])}')

