import time
from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="FastAPI Concurrency Example",
    description="A demonstration of FastAPI with asynchronous endpoints and concurrency handling",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Demo endpoint 1
# It shows time.sleep blocking the request and not allowing any other request to be processed
@app.get("/1")
async def endpoint1():
    print("Hello")
    time.sleep(10)
    print("Bye")
    return {"status": "Operation completed successfully"}