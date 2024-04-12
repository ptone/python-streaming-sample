import asyncio
from fastapi import FastAPI

app = FastAPI()
import time
from fastapi.responses import StreamingResponse

def stream_generator():
    for i in range(10):
        data = "iteration {} \n".format(i)
        print(data)
        yield data
        time.sleep(1)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/experimental/stream", summary="Experimenting with some streaming response stuff") 
async def stream_response():
    return(StreamingResponse(stream_generator()))