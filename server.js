let http = require("http");

let server = http.createServer((req, res) => {
    res.writeHead(200);
    console.log(req.url);
    res.end("hello");
});

server.listen(3001, () => {
    console.log("Server is running");
});