from fastapi import FastAPI

app = FastAPI()
import socket


@app.get("/")
def read_root():
    return {"hostname": socket.gethostname()}
