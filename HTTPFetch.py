import socket

class HTTPFetch:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.fail = False
    def connect(self, host, port):
        try:
            self.socket.connect((host, port))
        except ConnectionRefusedError:
            self.fail = "Connection refused !"
    def get(self, route=""):
        try:
            if not self.fail:
                request = "GET /{} HTTP/1.1\r\nHost:localhost\r\n\r\n".format(route)
                self.connect(self.host, self.port)
                self.socket.send(request.encode())
                return self.httpResponse()
        except BrokenPipeError:
            pass
        return self.fail
    def httpResponse(self):
        response = self.socket.recv(2048)
        self.socket.close()
        return response

request = HTTPFetch("localhost", 3000)
print(request.get("login"))