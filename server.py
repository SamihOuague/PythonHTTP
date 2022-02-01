import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 3001))
print(s.send(b'GET / HTTP/1.1\r\nHost:localhost/test\r\n\r\n'))
print(s.recv(255))
s.close()