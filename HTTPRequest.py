import socket

class HTTPRequest:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
    def connect(self, host, port):
        self.socket.connect((host, port))
    def get(self, route=""):
        request = "GET /{} HTTP/1.1\r\nHost:localhost\r\n\r\n".format(route)
        self.connect(self.host, self.port)
        self.socket.send(request.encode())
        return self.httpResponse()
    def httpResponse(self):
        response = self.socket.recv(255)
        self.socket.close()
        return response

request = HTTPRequest("localhost", 3000)

print(request.get("login"))