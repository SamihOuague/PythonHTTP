from HTTPResponse import *
import socket

class TinyServer:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def bindHost(self, host, port):
        self.s.bind((host, port))
        self.s.listen(5)
    def run(self, host="localhost", port=3001):
        try:
            self.bindHost(host, port)
            while True:
                (clientsock, address) = self.s.accept()
                response = HTTPResponse({'message': 'bonjour'})
                clientsock.recv(2048)
                print(response.end())
                clientsock.send(response.end())
            self.s.shutdown(1)
            self.s.close()
        except KeyboardInterrupt:
            self.s.shutdown(1)
            self.s.close()

server = TinyServer()
server.run()