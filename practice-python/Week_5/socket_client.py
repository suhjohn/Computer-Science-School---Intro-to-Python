import socket

host = 'localhost'
port = 12345
bufsiz = 4096
addr = (host, port)

if __name__ == '__main__':
	client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# input() or x 
	host = input("hostname[localhost]> ") or host
	port = input("port number[12345]> "))or port

	#connect
	sock_addr = (host, int(port))
	client_sock.connect(sock_addr)

	#payload : (1500bit단위로 잘려있는 = 패킷) 패킷에 있는 데이터
	payload = 'GET TIME'

	#send and receive info
	try :
		# 한번만 전송하고 끝나는 것이 아니기 때문에 필요할때까지 반복
		while True:
			#네트워크는 언제나 utf-8
			client_sock.send(payload.encode("utf-8"))
			data = client_sock.recv(bufsiz)
			"""
			an example code to explain repr
			import datetime
			today = datetime.datetime.now()
			repr(today)
			str(today)
			받는 데이터는 repr로 해야된다
			"""
			print(repr(data))

			more = input("Want more?[y/n")
			if more.lower() = 'y':
				#다른 데이터를 받고 싶을 때 요청
				payload = input("Enter payload: ")
			else:
				break
	except KeyboardInterrupt:
		print("Exited")

	client_sock.close()

	





