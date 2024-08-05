import uvicorn
from fastapi import FastAPI
from whisper.speech2text import app_whisper
from whisper.env import ADDRESS, PORT


app = FastAPI()
app.include_router(prefix="/api/v1",
                   router=app_whisper)

print(__name__)
if __name__ == "__main__":
    uvicorn.run("whisper.__main__:app", host=ADDRESS, port=PORT, reload=True)
