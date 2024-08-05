import os
from fastapi import File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
from whisper import whisper_model


app_whisper = APIRouter()


@app_whisper.post("/speech2text")
async def speech_to_text(audio: UploadFile = File(...), word_timestamps: bool = False) -> str:
    """Predict function."""
    path = os.path.join("whisper/data", audio.filename)

    # read and save wav file
    with open(path, "wb") as f:
        f.write(await audio.read())

    
    segments, _ = whisper_model.transcribe(path, word_timestamps=word_timestamps)

    if word_timestamps is False:
        result = ''.join([segment.text for segment in segments])
    else:
        result = [{
            'start': segment.start,
            'end': segment.end,
            'text': segment.text,
            'words': [{'start': word.start, 'end': word.end, 'word': word.word} for word in segment.words]
        } for segment in segments]

    # delete file
    os.remove(path)

    return JSONResponse(
        status_code=200,
        content={"result": result}
    )
