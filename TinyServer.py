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
                clientsock.recv(2048)
                clientsock.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nDate: Tue, 01 Feb 2022 10:59:16 GMT\r\nConnection: keep-alive\r\nKeep-Alive: timeout=5\r\nTransfer-Encoding: chunked\r\n\r\n14\r\n<h1>hello world</h1>\r\n0\r\n\r\n')
            self.s.shutdown(1)
            self.s.close()
        except KeyboardInterrupt:
            self.s.shutdown(1)
            self.s.close()

server = TinyServer()
server.run()