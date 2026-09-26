# Desktop Console Example

## Visual Layout

Here's what the **Anti-Drone Detection Console** looks like on a desktop browser:

```
╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  Anti-Drone Detection Console          Detection-only                14:32:45 26/09/2026  ║
╠═══════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                            ║
║  ┌─────────────────────────────────────────┐  ┌──────────────────┐                       ║
║  │ LIVE CAMERA FEED                        │  │ SYSTEM STATUS    │                       ║
║  │                                         │  │                  │                       ║
║  │   [Camera Stream from ESP32-CAM]        │  │ Backend: Online  │                       ║
║  │                                         │  │ Stream: --.--    │                       ║
║  │   or                                    │  │ Last update: 14:32:45                   ║
║  │                                         │  │                  │                       ║
║  │   Connect an ESP32-CAM stream to begin  │  └──────────────────┘                       ║
║  │                                         │                                              ║
║  └─────────────────────────────────────────┘  ┌──────────────────┐                       ║
║                                               │ DRONE DIRECTION  │                       ║
║                                               │    COMPASS       │                       ║
║                                               │                  │                       ║
║                                               │         N        │                       ║
║                                               │       ╱   ╲      │                       ║
║                                               │      ╱     ╲     │                       ║
║                                               │    W ● ↑ E  Red  │                       ║
║                                               │      ╲     ╱     │                       ║
║                                               │       ╲   ╱      │                       ║
║                                               │         S        │                       ║
║                                               │                  │                       ║
║                                               │ Bearing: 45°     │                       ║
║                                               │ Distance: 250m   │                       ║
║                                               └──────────────────┘                       ║
║                                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────────────────┐   ║
║  │ DETECTION EVENTS                                                                 │   ║
║  │                                                                                  │   ║
║  │ 14:32:12 - ALERT: Drone detected at bearing 45° (250m)                          │   ║
║  │ 14:31:58 - ALERT: Drone detected at bearing 270° (180m)                         │   ║
║  │ 14:31:22 - INFO: System initialized                                             │   ║
║  │                                                                                  │   ║
║  └──────────────────────────────────────────────────────────────────────────────────┘   ║
║                                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝
```

## Screen Elements

### Header
- **Title**: "Anti-Drone Detection Console"
- **Mode Badge**: "Detection-only"
- **Real-time Clock**: Shows HH:MM:SS DD/MM/YYYY (updates every second)

### Main Content (3 columns on desktop)

**Left Panel (Large - 2 columns wide)**
- Live camera feed from ESP32-CAM
- Placeholder text until stream connected
- Green/Red status indicator

**Top Right Panel**
- Backend status (Online/Offline)
- Stream URL status
- Last API update time

**Middle Right Panel**
- Compass visualization with cardinal directions (N, E, S, W)
- Red arrow pointing to detected drone bearing (0-360°)
- Bearing angle in degrees
- Distance in meters

**Bottom Panel (Full width)**
- Detection events log
- Timestamp + bearing + distance for each detection
- Scrollable event history

## Color Scheme

- **Background**: Dark blue (#0b1220)
- **Panels**: Darker blue (#111c30)
- **Text**: Light blue (#e5edf8)
- **Labels**: Medium blue (#91a4c2)
- **Accent (online)**: Green (#55d98c)
- **Alert (drone/error)**: Red (#ed6b76)
- **Borders**: Grid color (#263650)

## Responsive Design

- **Desktop (1200px+)**: 3-column layout as shown above
- **Tablet (700px-1200px)**: 2-column layout
- **Mobile (<700px)**: Single-column stacked layout

## Live Features

1. **Clock updates every 1 second** with new time/date
2. **Compass needle rotates** when drone is detected
3. **Status panel refreshes every 5 seconds**
4. **Events log appends new detections** with timestamps
5. **Color indicators change** based on system state

---

## To View on Your Computer

1. Start the server:
```bash
cd anti-drone-detector
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

2. Open browser:
```
http://127.0.0.1:8000
```

3. You'll see the dark-themed console with all the panels working in real-time!
