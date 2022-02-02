const express = require("express");
let app = express()

app.get("/", (req, res) => {
    res.send({"message": "welcome home"})
});
app.get("/admin", (req, res) => {
    res.send({"message": "not allowed here"})
})
app.get("/infos", (req, res) => {
    res.send({"message": "informations about us"})
})

app.listen(3000);