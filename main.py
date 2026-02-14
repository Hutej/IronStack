from IronBack import IronBack

app = IronBack()

@app.get("/users")
def get_user(request, response):
    response.send(400)
