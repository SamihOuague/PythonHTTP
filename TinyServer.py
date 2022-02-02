from HTTPResponse import *
from HTTPRequest import *
import socket

class TinyServer:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def bindHost(self, host, port):
        self.s.bind((host, port))
        self.s.listen(5)
    def run(self, express, port=3000):
        try:
            self.bindHost("localhost", port)
            while True:
                (clientsock, address) = self.s.accept()
                request = HTTPRequest(clientsock.recv(2048))
                response = HTTPResponse()
                clientsock.send(express.getRoute(request.getPath()))
            self.s.shutdown(1)
            self.s.close()
        except KeyboardInterrupt:
            self.s.shutdown(1)
            self.s.close()