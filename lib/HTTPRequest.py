class HTTPRequest:
    def __init__(self, req):
        self.req = req.decode().split("\r\n")
    def getPath(self):
        return self.req[0].split(" ")[1]