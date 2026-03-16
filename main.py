from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    image_path = "image.png"
    
    if os.path.exists(image_path):
        return FileResponse(image_path)
    
    return {"message": "error"}