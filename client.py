import socket
import sys
#create socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000;
host = socket.gethostbyname('localhost')


#connect socket to host
my_socket.connect((host, port))

#get user input and send to server
user_message = raw_input('Enter your message: ')
message = 'GET /echo.php?message='+user_message+' HTTP/1.0\r\n\r\n'
my_socket.sendall(message)


#recieve message from server and print
res = my_socket.recv(2048)
print "this is response: "
print res

#close the socket
my_socket.close()
