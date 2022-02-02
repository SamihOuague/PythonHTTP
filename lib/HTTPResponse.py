import json
import datetime
import sys

class HTTPResponse:
    def end(self, body):
        body = json.dumps(body)
        bodyLen = len(body)
        return "\r\n".join([
            "HTTP/1.1 200 OK",
            "Content-Type: application/json",
            "Date: {}".format(datetime.datetime.strftime(datetime.datetime.now(), "%a, %d %b %Y %H:%M:%S %Z")),
            "Connection: keep-alive",
            "Keep-Alive: timeout=5",
            "Transfer-Encoding: chunked",
            "",
            hex(bodyLen).split("x")[1],
            body,
            "0",
            "",
            "",
        ]).encode("utf-8")