#!/usr/bin/python
'''
	(C) x-c0der
	Slides.js Remote Server 
'''

import socket
import sys
from thread import *

s = socket.socket()
print 'Socket created'

HOST = ''
PORT = 5124

CLIENT_LIST = []
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

def public_broadcast_message(conn, addr, data):
	for client in CLIENT_LIST:
		if client != conn:
			print data
			client.send('\n')
			client.send('<' + addr[0] + '>: ' + data)
			client.send("<You>: ")


def clientthread(conn, addr):

	_first_send = '''
This is a global chat Please dont Abuse
IP Address is logged with every message
(C) ANAND SIDDHARTH #x-c0der

Welcome to chat.anandsiddharth.in
Chat Server.
You can Chat As well as view list of commands by typing command: <this is a command> For e.g command: help

If you are sure you follow the rules hit and enter and start conversation
'''
	conn.send(_first_send)

	while True:
	        #Receiving from client
		data = conn.recv(1024)
		conn.send("<You>: ")
		if len(data) != 0 and data != '' and data != ' ':
			public_broadcast_message(conn, addr, data)
		# print conn, data
		if not data:
			break
	            
	conn.close()
while 1:
	conn, addr = s.accept()
	CLIENT_LIST.append(conn)
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	start_new_thread(clientthread ,(conn, addr,))
s.close()
