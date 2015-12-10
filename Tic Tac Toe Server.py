#!/usr/bin/python3          
import socket, select         # Import socket module
import time
class TicTacToe:
	def __init__(self, port=12345):
		self.connections = []                 # List of connections
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
				
				if addr not in self.connections:				#if the client isn't in the list
					self.connections.append(c) 				# Add client to list of connections
					print("\nINFO:: Got connection from" + str(addr) +"\nINFO:: Adding to client list")
					if len(self.connections) == 1: 				# If there is 1 connection send a 'X' to the last added connection
						assignTurn = "X"
						self.connections[0].send(assignTurn.encode('utf-8'))
					elif len(self.connections) == 2: 			# If there is 2 connections send a 'O' to the last added connection
						assignTurn = "O"
						self.connections[1].send(assignTurn.encode('utf-8'))
				

			else:
				msgbytes = conn.recv(1024) 					#Recieve a number from 0-8 defining which square was picked
				msgbytes = msgbytes.decode('utf-8').rstrip('\r\n')		#Decode the message
				print ("INFO:: Square " + str(msgbytes) + " was played")
				print ("INFO:: Sending that move to the other client...")
				for client in self.connections: 				#Send the number to the other clients
					if conn != client:					#But don't send it back to it self
						client.send(msgbytes.encode('utf-8'))		#encode the message
						print("INFO:: Move sent to the other client\n")
				

				if not msgbytes: 						# if the server receives an empty message
					print('Disconnected')					# then disconnect


#--------------------------------------------------------------------------Start the server---------------------------------------------------------------------------------
#Prints to tell the user that the server has started and the ip address it is running on
print("INFO:: Starting Tic Tac Toe Server")
print("INFO:: The Servers ip is " + socket.gethostbyname(socket.gethostname()))
print("INFO:: Binding to port: 12345\n")
time.sleep(1)
print("INFO:: Server ready for clients to connect")


if __name__ == '__main__':
	try:
		c = TicTacToe()
		while True:
			c.poll()
	except KeyboardInterrupt:
		c.shutdown()
							
