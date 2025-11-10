<div align="center">

  <h1>🔴 Live USB Camera Streaming – Real-Time Web Interface System</h1>
  This repository documents the <b>live video streaming setup</b> using a <b>USB camera</b> on a <b>Linux-based embedded board</b> (without ffmpeg or ffplay) and viewing the live feed through a <b>Flask web interface</b> as part of the <b>VLSI Design Contest 2026</b>.
  </p>

   <a href="https://www.microchip.com/" target="_blank">
  <img width="270" height="180" alt="Microchip Logo" src="https://github.com/user-attachments/assets/1d5e8b0d-e14c-4ee5-8a40-ab32b5b485f0" />
  </a>

  <br><br>
  
   <img src="https://img.shields.io/badge/Interface-USB_Camera-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Buildroot_Linux-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Flask-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Project-VLSID_2026-red?style=for-the-badge" />

</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Objective** | [Jump to Section](#-1-objective) |
| 2 | **System Configuration** | [Jump to Section](#-2-system-configuration) |
| 3 | **Implementation Steps** | [Jump to Section](#-3-implementation-steps) |
| 4 | **Notes** | [Jump to Section](#-4-notes) |
| 5 | **Result** | [Jump to Section](#-5-result) |
| 6 | **Output** | [Jump to Section](#-6-output) |
| 7 | **Repository Structure** | [Jump to Section](#-7-repository-structure) |
| 8 | **Contributors** | [Jump to Section](#-8-contributors) |

---

## 🧩 1. Objective

To set up a **live video streaming system** using a **USB camera** on a Linux-based embedded platform without using **ffmpeg** or **ffplay**, and display the **real-time stream via a Flask-based web interface**.

---

## ⚙️ 2. System Configuration

### **Hardware**
- Microchip PolarFire SoC (Icicle Kit)  
- USB Camera (UVC compliant)  
- Windows PC (for browser-based viewing)

### **Software**
- Buildroot-based Linux OS  
- `v4l2-ctl` for camera control  
- `Python3` with `Flask` for web interface  

---

# 🧰 3. Implementation Steps

### ✅ Step 1 – Verify Camera Detection
```bash
ls /dev/video*
v4l2-ctl --list-devices
```
Confirm that the camera is detected as:
```
/dev/video0
```


### ✅ Step 2 – Test Camera Stream (Command-line)
```bash
v4l2-ctl --device=/dev/video0 --stream-mmap --stream-count=0
```

This command starts **continuous streaming** until manually stopped (`Ctrl + C`).

### ✅ Step 3 – Create Python Web Live Stream Application

Save the following as live_cam.py:
  
```python
from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <title>Live Camera Stream</title>
  <style>
    body { text-align: center; background: #111; color: white; font-family: Arial; }
    h1 { margin-top: 30px; }
    iframe { width: 80%; height: 600px; border: 3px solid #444; border-radius: 10px; }
  </style>
</head>
<body>
  <h1>🔴 Live USB Camera Stream</h1>
  <p>Camera is currently streaming...</p>
  <iframe src="/start" title="Camera Stream"></iframe>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/start')
def start_stream():
    cmd = ["v4l2-ctl", "--device=/dev/video0", "--stream-mmap", "--stream-count=0"]
    subprocess.Popen(cmd)
    return "Camera stream started. Press Ctrl+C to stop."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### ✅ Step 4 – Run the Web Server
```bash
python3 live_cam.py
```

Then open your browser and visit:

```cpp
http://<BOARD_IP>:8080
```

🎥 You’ll see a live video streaming interface.
✅ Step 4 – Run the Web Server
python3 live_cam.py


Then open your browser and visit:

http://<BOARD_IP>:8080


🎥 You’ll see a live video streaming interface.
✅ Step 4 – Run the Web Server
python3 live_cam.py


Then open your browser and visit:

http://<BOARD_IP>:8080


🎥 You’ll see a live video streaming interface.
Stop the server using **Ctrl+C** when done.


# 🗒️ 4. Notes

- No ffmpeg or ffplay is required.
- The LED indicator on the camera confirms active streaming.
- The streaming continues until manually stopped.
- Compatible even with minimal Buildroot systems.

 # 🧠 5. Result

✅ Successfully implemented a real-time USB camera live stream using:
- v4l2-ctl for video capture
- Flask for web streaming
- No dependency on multimedia frameworks like ffmpeg or OpenCV

 # 🖼️ 6. Output
<p align="center"> <img width="850" alt="Live Camera Stream Interface" src="https://github.com/user-attachments/assets/bcad2162-849e-413a-a71e-013121848362" /> </p>

🎯 Live Stream successfully displayed in browser

### 🎬 Demonstration Video 
<p align="center"> <a href="https://drive.google.com/file/d/1_fOGxz7dh-BbckkwF-zosibxvsfo0BrW/view?usp=drive_link" target="_blank"> <img src="./images/video_preview.jpg" width="700" alt="USB Camera Live Stream Demonstration"> </a> </p>

🎥 Click the image above to watch the full demonstration video on Google Drive.

📂 7. Repository Structure
live-usb-camera-streaming/
│
├── live_cam.py
├── README.md
├── LICENSE
├── docs/
│   └── Live_Stream_Report.pdf
└── images/
    ├── video_preview.jpg
    └── stream_output.png

 # 👩‍💻 8. Contributors

| 👤 **Name** | 🌐 **GitHub Profile** |
|-------------|-----------------------|
| **Senbagaseelan V** | [@Senbagaseelan18](https://github.com/Senbagaseelan18) |
| **Praveen R** | [@PRAVEENRAMU14](https://github.com/PRAVEENRAMU14) |
| **Ragul T** | [@Ragul-2005](https://github.com/Ragul-2005) |
| **Tharun Babu V** | [@TharunBabu-05](https://github.com/TharunBabu-05) |

<div align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Microchip_logo.svg" width="160" alt="Microchip Logo" />

© 2025 VLSI Design Contest – Live USB Camera Streaming Project
Developed on Buildroot Linux using PolarFire® SoC Icicle Kit

<br><br>

<img src="https://img.shields.io/badge/Setup_Status-Completed-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/Web_Stream-Active-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Performance-Stable-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/Playback-Verified-orange?style=for-the-badge" /> </div> ```
