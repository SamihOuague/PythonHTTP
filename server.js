let http = require("http");

let server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "application/json");
    res.writeHead(200);
    res.end('{"test": "teste", "te": "t"}');
});

server.listen(3000);