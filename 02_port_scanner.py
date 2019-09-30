"""
Port Scanner will scan and tell whether a port is Open or closed
"""

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'www.google.com'

def port_scan(server, port):
	"""
	this function will take an server and port number as an input
	and return whether that port number is open(True) or close(False)
	"""
	try:
		soc.connect(server, port)
		return True
	except:
		return False


if __name__ == '__main__':
	
	for port in range(1, 26):
		if port_scan(server, port):
			print(f'Port {port} is open')
		else:
			print(f'Port {port} is closed')