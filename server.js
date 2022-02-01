let http = require("http");

let server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "application/json");
    res.writeHead(200);
    res.end("{'message': 'bonjour'}");
});

server.listen(3000);