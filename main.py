from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def grandma():
    return "Works nicely"
