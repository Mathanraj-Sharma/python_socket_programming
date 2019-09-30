import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'Socket: {soc}')

server = 'www.google.com'
port = 80

server_ip = socket.gethostbyname(server)
print(f'Server IP: {server_ip}')

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

soc.connect((server, port))
soc.send(request.encode())

# 4096 if the buffer size
result = soc.recv(4096) 

while (len(result) > 0):
	print(result)
	result = soc.recv(4096)