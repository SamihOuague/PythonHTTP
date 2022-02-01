let http = require("http");

let server = http.createServer((req, res) => {
    res.writeHead(200);
    res.end("<h1>hello wor</h1>");
});

server.listen(3000);