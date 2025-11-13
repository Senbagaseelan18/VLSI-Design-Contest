<div align="center">

  <h1>🟢 Real-Time Speech-to-Text on PolarFire SoC Icicle Kit – Web Interface</h1>
  <p>
  This repository implements a <strong>real-time speech-to-text system</strong> running directly on the  
  <strong>Microchip PolarFire SoC Icicle Kit (RISC-V)</strong> using <strong>Flask</strong>, <strong>ALSA (arecord)</strong>, and <strong>Python SpeechRecognition</strong>.  
  The system captures audio using <strong>arecord</strong>, processes it via <strong>Google's Speech API</strong>, and displays  
  the recognized text live on a <strong>web dashboard</strong>, without requiring PyAudio or Vosk.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
  <img width="270" height="180" alt="Microchip Logo" src="https://github.com/user-attachments/assets/1d5e8b0d-e14c-4ee5-8a40-ab32b5b485f0" />
  </a>

  <br><br>

  <img src="https://img.shields.io/badge/Speech_Engine-Google_API-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Flask-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Buildroot_Linux-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Audio_ALSA-arecord-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Application-Embedded_AI-green?style=for-the-badge" />

</div>

---

## 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Introduction** | [Jump to Section](#-1-introduction) |
| 2 | **Buildroot Configuration** | [Jump to Section](#-2-buildroot-configuration) |
| 3 | **Menuconfig Setup** | [Jump to Section](#-3-menuconfig-setup) |
| 4 | **Post-Build Script** | [Jump to Section](#-4-post-build-script) |
| 5 | **Build Process** | [Jump to Section](#-5-build-process) |
| 6 | **On-Board Implementation** | [Jump to Section](#-6-on-board-implementation) |
| 7 | **Run the Application** | [Jump to Section](#-7-run-the-application) |
| 8 | **Output** | [Jump to Section](#-8-output) |
| 9 | **Contributors** | [Jump to Section](#-9-contributors) |

---

## 🟩 1. Introduction

This project demonstrates a **lightweight speech-to-text pipeline** running directly on the  
**PolarFire SoC Icicle Kit (RISC-V, Buildroot Linux)**.  
It converts live microphone input into readable text using:

- **ALSA arecord** for audio capture  
- **Python SpeechRecognition** for cloud-based recognition  
- **Google Speech API** for translation to text  
- **Flask** for a real-time web user interface  

The system shows that **PyAudio and Vosk are not necessary** — everything runs using minimal components already supported by the board.

---

## 🟩 2. Buildroot Configuration

### 📌 Buildroot Path  
```
/home/senba/buildroot/buildroot/
```

### 📌 Files Modified
- `configs/microchip_mpfs_icicle_defconfig`
- `system/post-build.sh`

### 📌 Added to Defconfig
```
BR2_ROOTFS_POST_BUILD_SCRIPT="system/post-build.sh"
```

---

## 🟩 3. Menuconfig Setup

To support Python-based speech recognition and ALSA audio, enable:

### ✅ Python  
`Target packages → Interpreter languages → python3`

### ✅ pip  
`Target packages → python3 → python3-pip`

### ✅ Required Python Modules  
`Target packages → Python modules`
- flask  
- numpy  
- requests  
- openai  
- sounddevice  
- SpeechRecognition  

### ✅ ALSA Audio Support  
`Target packages → Audio and video applications`
- alsa-utils  
- alsa-lib  

### Optional  
- espeak  
- flite  

---

## 🟩 4. Post-Build Script

📌 **Path:**  
```
/home/senba/buildroot/buildroot/system/post-build.sh
```

📌 **Purpose:**  
Install Python libraries directly into the target root filesystem.

### 📄 Script:
```bash
#!/bin/bash
set -e
TARGET_DIR=$1
PYTHON_DIR="${TARGET_DIR}/usr/lib/python3.12/site-packages"
HOST_WHEELS_DIR="/home/senba/buildroot/buildroot/dl/python_wheels"

mkdir -p ${PYTHON_DIR}
mkdir -p ${TARGET_DIR}/python_wheels

/usr/bin/python3 -m pip install --no-index \
  --find-links=${HOST_WHEELS_DIR} \
  --target=${PYTHON_DIR} \
  flask numpy requests openai SpeechRecognition
```

---

## 🟩 5. Build Process

```bash
cd /home/senba/buildroot/buildroot
make clean
make microchip_mpfs_icicle_defconfig
make 2>&1 | tee build.log
```

📌 **Final Image:**
```
/home/senba/buildroot/buildroot/output/images/sdcard.img
```
Flash to SD card → Boot Icicle Kit.

---

## 🟩 6. On-Board Implementation

### 1️⃣ Check Installed Packages
```bash
python3 --version
pip --version
python3 -m pip list
```

### 2️⃣ Create Application Directory
```bash
mkdir /root/speech_web
cd /root/speech_web
```

### 3️⃣ Create Flask + SpeechRecognition App
```bash
cat > app_google.py <<'EOF'
from flask import Flask, render_template_string, jsonify
import speech_recognition as sr
import threading
import subprocess
import os
import time

app = Flask(__name__)

# Global variables
recognized_text = ""
is_recording = False
recording_thread = None

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Real-Time Speech-to-Text</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 30px;
        }
        #transcript {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            margin: 30px auto;
            max-width: 800px;
            min-height: 200px;
            font-size: 1.5em;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        button {
            font-size: 1.5em;
            padding: 15px 40px;
            margin: 10px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        #startBtn {
            background: #4CAF50;
            color: white;
        }
        #stopBtn {
            background: #f44336;
            color: white;
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }
        .status {
            font-size: 1.2em;
            margin: 20px;
        }
    </style>
</head>
<body>
    <h1>🎤 Real-Time Speech-to-Text</h1>
    <div class="status">Status: <span id="status">Ready</span></div>
    <button id="startBtn" onclick="startRecording()">Start Recording</button>
    <button id="stopBtn" onclick="stopRecording()">Stop Recording</button>
    <div id="transcript">Waiting for speech...</div>

    <script>
        function startRecording() {
            fetch('/start')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('status').textContent = 'Recording...';
                    document.getElementById('startBtn').disabled = true;
                    document.getElementById('stopBtn').disabled = false;
                });
        }

        function stopRecording() {
            fetch('/stop')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('status').textContent = 'Stopped';
                    document.getElementById('startBtn').disabled = false;
                    document.getElementById('stopBtn').disabled = true;
                });
        }

        function updateTranscript() {
            fetch('/get_text')
                .then(response => response.json())
                .then(data => {
                    if (data.text) {
                        document.getElementById('transcript').textContent = data.text;
                    }
                });
        }

        setInterval(updateTranscript, 1500);
    </script>
</body>
</html>
'''

def record_audio():
    global recognized_text, is_recording
    recognizer = sr.Recognizer()
    
    while is_recording:
        try:
            # Record audio using arecord
            audio_file = "/tmp/speech.wav"
            subprocess.run([
                "arecord", "-D", "plughw:0,0", "-f", "S16_LE", 
                "-r", "16000", "-d", "5", audio_file
            ], check=True)
            
            # Recognize speech
            with sr.AudioFile(audio_file) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio)
                recognized_text += text + " "
                print(f"Recognized: {text}")
            
            # Clean up
            os.remove(audio_file)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/start')
def start_recording():
    global is_recording, recording_thread, recognized_text
    if not is_recording:
        recognized_text = ""
        is_recording = True
        recording_thread = threading.Thread(target=record_audio)
        recording_thread.start()
    return jsonify({"status": "started"})

@app.route('/stop')
def stop_recording():
    global is_recording
    is_recording = False
    return jsonify({"status": "stopped"})

@app.route('/get_text')
def get_text():
    return jsonify({"text": recognized_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
EOF
```
![](https://raw.githubusercontent.com/Senbagaseelan18/VLSI-Design-Contest/main/Speech_to_text_web/Images/1.png)


---

## 🟩 7. Run the Application

```bash
cd /root/speech_web
python3 app_google.py
```
![](https://raw.githubusercontent.com/Senbagaseelan18/VLSI-Design-Contest/main/Speech_to_text_web/Images/2.png)


### Access from Browser
```
http://<board-ip>:8080
```

---

## 🟩 8. Output
![](https://raw.githubusercontent.com/Senbagaseelan18/VLSI-Design-Contest/main/Speech_to_text_web/Images/3.png)
![](https://raw.githubusercontent.com/Senbagaseelan18/VLSI-Design-Contest/main/Speech_to_text_web/Images/4.png)

✅ Real-time transcription  
✅ Start/Stop recording  
✅ Flask live dashboard  
✅ Recognized text auto-refreshes every 1.5 sec  
✅ Works without PyAudio or Vosk  

---

## 👩‍💻 9. Contributors

| 👤 **Name** | 🌐 **GitHub Profile** |
|-------------|-----------------------|
| **Senbagaseelan V** | [@Senbagaseelan18](https://github.com/Senbagaseelan18) |
| **Praveen R** | [@PRAVEENRAMU14](https://github.com/PRAVEENRAMU14) |
| **Ragul T** | [@Ragul-2005](https://github.com/Ragul-2005) |
| **Tharun Babu V** | [@TharunBabu-05](https://github.com/TharunBabu-05) |

---

<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Microchip_logo.svg" width="160" alt="Microchip Logo" />

**© 2025 VLSI Design Contest – Real-Time Speech-to-Text Project**  
**Developed on Buildroot Linux using PolarFire® SoC Icicle Kit**

<br><br>

<img src="https://img.shields.io/badge/Setup_Status-Completed-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Speech_Recognition-Active-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/Performance-Optimized-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Web_Interface-Verified-orange?style=for-the-badge" />

<br><br>

⭐ **If you found this project useful, don't forget to star this repository!**

</div>
