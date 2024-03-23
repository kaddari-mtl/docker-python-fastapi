from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def index():
    return {"message", f"hello! Secret = {os.environ['MY_ENV_VARIABLE']}"}