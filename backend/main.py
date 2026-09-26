"""Anti-drone detection console backend."""
from datetime import datetime, timezone
from pathlib import Path
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Anti-Drone Detection Console")
BASE = Path(__file__).parent
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")

@app.get("/")
def dashboard():
    return FileResponse(BASE / "static" / "index.html")

@app.get("/api/status")
def status():
    return {
        "ok": True,
        "mode": "detection-only",
        "stream_url": os.getenv("ESP32_STREAM_URL", ""),
        "time": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/api/events")
def events():
    # Replace this with SQLite-backed events after the camera pipeline is connected.
    return {"events": []}
