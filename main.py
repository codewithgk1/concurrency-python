import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

# Demo endpoint 1
# It shows time.sleep blocking the request and not allowing any other request to be processed
# This is a blocking operation and will block the entire server for 10 seconds

###
# Runs in main thread
# No awaitable operations, cannot be paused
# Sequential order
# Request 1
#   Hello
#   Bye
# Request 2
#   Hello
#   Bye
###
@app.get("/1")
async def endpoint1(): # Processed Sequentially
    print("Hello")
    time.sleep(10) # Blocking I/O operation,can not be awaited,
    # Function execution can not be paused and wait for the operation to complete
    print("Bye")
    return {"status": "Operation completed successfully"}


# Demo endpoint 2
# It shows asyncio.sleep not blocking the request and allowing other requests to be processed
# This is a non-blocking operation and will not block the entire server
###
# Runs in main thread
# Has awaitable operations, can be paused
# Request 1
#   Hello
# Request 2 
#   Hello
# Request 1 
#   Bye
# Request 2 
#   Bye
###
@app.get("/2")
async def endpoint2(): # Processed Concurrently
    print("Hello from endpoint 2")
    await asyncio.sleep(10) # Non Blocking I/O operation, awaited,
    # Function execution paused
    print("Bye from endpoint 2")
    return {"status": "Operation completed successfully"}


##
# Runs in seperate Threads like asyncio.sleep
##
# Demo endpoint 3
@app.get("/3")
def endpoint3():
    print("Hello")
    time.sleep(10)
    print("Bye")
    return {"status": "Operation completed successfully"}



#
# Uvicorn -> Main Thread
# Coroutines -> Event Loop which runs in main thread
# 
#