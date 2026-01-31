from IronBack import IronBack

app = IronBack()

@app.get("/user")
def get_user(request, response):
    response["status_code"] = "200 OK"
    response["headers"] = []
    response["text"] = "['hutej'], ['mane']"
