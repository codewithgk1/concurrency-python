import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

# Demo endpoint 1
# It shows time.sleep blocking the request and not allowing any other request to be processed
# This is a blocking operation and will block the entire server for 10 seconds
@app.get("/1")
async def endpoint1():
    print("Hello")
    time.sleep(10)
    print("Bye")
    return {"status": "Operation completed successfully"}


# Demo endpoint 2
# It shows asyncio.sleep not blocking the request and allowing other requests to be processed
# This is a non-blocking operation and will not block the entire server
@app.get("/2")
async def endpoint2():
    print("Hello")
    await asyncio.sleep(10)
    print("Bye")
    return {"status": "Operation completed successfully"}