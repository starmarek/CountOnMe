from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def grandma():
    return "Works nicely"


@app.get("/grandma/")
def grandma2():
    return "Works nicelyyyyyyy"
