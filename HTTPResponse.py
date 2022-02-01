import json
import datetime

class HTTPResponse:
    def __init__(self, body={}):
        self.body = json.dumps(body)
    def end(self):
        bodyLen = len(self.body)
        return "\r\n".join([
            "HTTP/1.1 200 OK",
            "Content-Type: application/json",
            "Date: {}".format(datetime.datetime.strftime(datetime.datetime.now(), "%a, %d %b %Y %H:%M:%S %Z")),
            "Connection: keep-alive",
            "Keep-Alive: timeout=5",
            "Transfer-Encoding: chunked",
            "",
            str(bodyLen - 2),
            self.body,
            "0",
            "",
            "",
        ]).encode("utf-8")