from HTTPResponse import *
from TinyServer import *

class Express:
    def __init__(self):
        self.routes = {"404": self.notFound}
    def get(self, route, fnCallback):
        self.routes[route] = fnCallback
    def notFound(self, res):
        return res.end({"error": "Not Found !"})
    def getRoute(self, path):
        try:
            response = HTTPResponse()
            return self.routes[path](response)
        except KeyError:
            response = HTTPResponse()
            return self.routes["404"](response)
    def listen(self, port):
        server = TinyServer()
        server.run(self, port)