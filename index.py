from lib import Express

app = Express.Express()

def home(res):
    return res.end({"message": "welcome home"})

def admin(res):
    return res.end({"message": "not allowed here"})

def infos(res):
    return res.end({"message": "informations about us"})

app.get("/", home)
app.get("/admin", admin)
app.get("/infos", infos)

app.listen(3000)