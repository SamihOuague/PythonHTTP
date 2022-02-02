from lib import HTTPResponse
from lib import TinyServer

class Express:
    def __init__(self):
        self.routes = {"404": self.notFound}
    def get(self, route, fnCallback):
        self.routes[route] = fnCallback
    def notFound(self, res):
        return res.end({"error": "Not Found !"})
    def getRoute(self, path):
        try:
            response = HTTPResponse.HTTPResponse()
            return self.routes[path](response)
        except KeyError:
            response = HTTPResponse.HTTPResponse()
            return self.routes["404"](response)
    def listen(self, port):
        server = TinyServer.TinyServer()
        server.run(self, port)