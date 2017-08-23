import socket
from time import ctime


host  = 'localhost'
port = 3080
bufsiz = 1024
#host 와 port 를 묶어서 addr 정의
addr = (host, port)

if __name__ == '__main__':
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(addr)
	server_socket.listen(5)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 3)

	while True:
		print("Server is listening..")
		client_sock, addr = server_socket.accept()
		print("Client conneted from : ", addr)

		while True:
			data = client_sock.recv(bufsiz)
			if not data or data.decode("utf-8") == 'END' :
				break

			print("received data from client: %s" % data.decode("utf-8"))
			print("Sending Server time: %s" % ctime())

			# Error handling
			try: 
				client_sock.send(bytes(ctime(), 'utf-8'))
			except KeyboardInterrupt:
				print("Exited by user")


	# 서버가 들어오는 포트번호는 매번 다르다, 즉 클라이언트는 집을 들어갈 때 항시 다른 포탈 문을 타는거라 생각하면 된다. 