from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse 

app = FastAPI()

origins = ["*"]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/home")
async def home():
    return FileResponse("index.html")

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')