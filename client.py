import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8000;
host = socket.gethostbyname('localhost')



my_socket.connect((host, port))
message = 'GET /echo.php?message=x HTTP/1.0\r\n\r\n'
my_socket.sendall(message)



res = my_socket.recv(2048)
print "this is response: "
print res
my_socket.close()
