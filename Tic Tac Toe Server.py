#!/usr/bin/python3          
import socket, select         # Import socket module
import time

class Chat:
	def __init__(self, port=12345):
		self.connections = []
		self.clients = []

		self.server = socket.socket()         # Create a socket object
		self.server.bind(('', port))          # Bind to the port
		self.server.listen(5)                 # Now wait for client connection.

	def shutdown(self):
		for c in self.connections:
			c.close()

		self.server.shutdown(1)
		self.server.close()

	def poll(self):
		read, write, error = select.select( self.connections+[self.server], self.connections, self.connections, 0 )

		for conn in read:
			if conn is self.server: 						# new client connecting
				c, addr = conn.accept()
				
				if addr not in self.connections:
					self.connections.append(c)
					print("\nINFO:: Got connection from" + str(addr) +"\nINFO:: Adding to client list")
					if len(self.connections) == 1:
						assignTurn = "X"
						self.connections[0].send(assignTurn.encode('utf-8'))
					elif len(self.connections) == 2:
						assignTurn = "O"
						self.connections[1].send(assignTurn.encode('utf-8'))
				

			else:
				msgbytes = conn.recv(1024)
				msgbytes = msgbytes.decode('utf-8').rstrip('\r\n')
				print ("INFO:: Square " + str(msgbytes) + " was played")
				print ("INFO:: Sending that move to the other client...")
				for client in self.connections:
					if conn != client:
						client.send(msgbytes.encode('utf-8'))
						print("INFO:: Move sent to the other client\n")
				

				if not msgbytes: 						# treat empty message as a disconnection
					print('Disconnected')


print("INFO:: Starting Tic Tac Toe Server")
time.sleep(1)
print("INFO:: Server ready for clients to connect")


if __name__ == '__main__':
	try:
		c = Chat()
		while True:
			c.poll()
	except KeyboardInterrupt:
		c.shutdown()
							
