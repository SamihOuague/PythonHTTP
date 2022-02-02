from Express import *

app = Express()

def home(res):
    return res.end({"message": "welcome home"})

def admin(res):
    return res.end({"message": "not allowed here"})

def infos(res):
    return res.send({"message": "informations about us"})

app.get("/", home)
app.get("/admin", admin)
app.get("/infos", infos)

app.listen(3001)