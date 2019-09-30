import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = "www.google.com"

def port_scan(port):
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		connection = soc.connect((target, port))
		with print_lock:
			print(f'Port {port} is open!')

		connection.close()

	except:
		pass


def threader():
	"""
	task that each thread has to do
	"""
	while True:
		worker = q.get()
		port_scan(worker)
		q.task_done()



if __name__ == '__main__':
	q = Queue()

	#number of threads
	for worker in range(50):
		t = threading.Thread(target = threader)
		t.daemon = True
		t.start()

	for port in range(1, 101):
		q.put(port)

	q.join()

