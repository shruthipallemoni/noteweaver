from fastapi import FastAPI

app = FastAPI(title="NoteWeaver API")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "NoteWeaver backend is alive"}