# Anti-Drone Detector

Detection-only prototype for an ESP32-CAM video source and a local console. It displays a live stream, detection events, and system status. It does **not** jam, take control of, or disable aircraft.

## Structure

- `backend/` — FastAPI console API and static dashboard
- `firmware/esp32_cam_sender/` — minimal ESP32-CAM sender guidance
- `data/` — local event storage (created at runtime)

## Quick start

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open http://127.0.0.1:8000.

Set `ESP32_STREAM_URL` to the ESP32-CAM MJPEG URL before starting the server. The current dashboard can also be used with a browser-accessible stream URL.

## Safety and privacy

Use only on property and airspace where you have authorization. Follow local aviation, privacy, and radio regulations. This project is for observation and alerting only.
