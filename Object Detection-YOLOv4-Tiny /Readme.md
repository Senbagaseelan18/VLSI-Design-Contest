<div align="center">

  <h1>🟢 YOLOv4-Tiny Object Detection – Single-Image Web Interface</h1>
  <p>
  This repository implements a **single-image object detection system** on an **embedded Buildroot Linux board** using **YOLOv4-Tiny** with **OpenCV DNN** and a **Flask web interface**.  
  The system captures one frame from a **USB camera**, performs **object detection**, and displays the detected result instantly on a webpage.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
  <img width="270" height="180" alt="Microchip Logo" src="https://github.com/user-attachments/assets/1d5e8b0d-e14c-4ee5-8a40-ab32b5b485f0" />
  </a>

  <br><br>

  <img src="https://img.shields.io/badge/Model-YOLOv4_Tiny-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Flask-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Buildroot_Linux-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Interface-USB_Camera-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Application-Embedded_AI-green?style=for-the-badge" />

</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Introduction** | [Jump to Section](#-1-introduction) |
| 2 | **Buildroot Configuration** | [Jump to Section](#-2-buildroot-configuration) |
| 3 | **Directory Setup** | [Jump to Section](#-3-directory-setup) |
| 4 | **Download Required Model Files** | [Jump to Section](#-4-download-required-model-files) |
| 5 | **Create Python Application** | [Jump to Section](#-5-create-python-application) |
| 6 | **Run the Application** | [Jump to Section](#-6-run-the-application) |
| 7 | **Performance Results** | [Jump to Section](#-7-performance-results) |
| 8 | **Output** | [Jump to Section](#-8-output) |
| 9 | **Contributors** | [Jump to Section](#-9-contributors) |

---

## 🔹 1. Introduction

The goal of this project is to implement **real-time object detection** on an embedded board using the **YOLOv4-Tiny** model — without requiring **PyTorch** or **ONNX**.  
Instead, the system uses **OpenCV's DNN module** for inference, making it lightweight and suitable for **CPU-only embedded environments**.

To minimize latency, the system captures a **single frame** each time the user clicks the **Capture Image** button in the web interface.  
The captured image is processed with **YOLOv4-Tiny**, and the output is shown instantly in the browser.

---

## 🔹 2. Buildroot Configuration

### 🧩 Required Packages in make menuconfig

### 🐍 Python Configuration
```css
Target packages --->
    Interpreter languages and scripting --->
        [*] python3
        [*] python3-pip
        [*] python3-numpy
        [*] python3-pillow
        [*] python3-requests
        [*] python3-flask
```

### 🎥 OpenCV Configuration
```css
Target packages --->
    Graphic libraries and applications --->
        opencv4 --->
            [*] dnn
            [*] highgui
            [*] video
            [*] videoio
            [*] imgproc
            [*] objdetect
            [*] gstreamer-1.x
            [*] ffmpeg
            [*] v4l
            [*] png
            [*] jpeg
            [*] webp
```

### ⚙️ Utilities
```css
Hardware handling --->
    [*] v4l2-utils
Networking applications --->
    [*] ca-certificates
    [*] wget
```

### ✅ Purpose Summary:

| Category | Package | Function |
|----------|---------|----------|
| Python | Flask, Numpy, Pillow | Web + Image Processing |
| OpenCV | DNN, VideoIO | Model inference + Camera interface |
| Hardware | v4l2-utils | Control exposure & formats |
| Network | ca-certificates | HTTPS model downloads |

---

## 🔹 3. Directory Setup

Create a working directory for model files and your application.

```bash
# Create project directory
mkdir -p /root/models_V4
cd /root/models_V4
```

---

## 🔹 4. Download Required Model Files

Since Buildroot lacks SSL certificates by default, use the `--no-check-certificate` flag.

```bash
# Download YOLOv4-Tiny config and weights
wget --no-check-certificate https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
wget --no-check-certificate https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights

# Download COCO class labels
wget --no-check-certificate https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

# Confirm files
ls -lh
# Expected: yolov4-tiny.cfg, yolov4-tiny.weights, coco.names
```

<p align="center">
  <img src="https://github.com/Senbagaseelan18/VLSI-Design-Contest/blob/main/Object%20Detection-YOLOv4-Tiny/Images/yolov4.png" width="1000" alt="YOLOv4-Tiny Object Detection Banner">
</p>



<p align="center">
  <img src="https://github.com/Senbagaseelan18/VLSI-Design-Contest/blob/main/Object%20Detection-YOLOv4-Tiny/Images/yolov2.png" width="1000" alt="YOLOv4-Tiny Object Detection">
</p>


---

## 🔹 5. Create Python Application

Create the Python file:

```bash
nano /root/models_V4/obj1.py
```

Paste the following complete code:

```python
import cv2
import numpy as np
from flask import Flask, request, send_file
import os, time, subprocess

# ==================== Configuration ====================
MODEL_CFG = "/root/models_V4/yolov4-tiny.cfg"
MODEL_WEIGHTS = "/root/models_V4/yolov4-tiny.weights"
CLASSES_FILE = "/root/models_V4/coco.names"
OUTPUT_IMAGE = "/tmp/detected.jpg"
CAMERA_DEVICE = 0  # /dev/video0

# ==================== Load YOLO Model ====================
print("[INFO] Loading YOLOv4-tiny model...")
if not os.path.exists(MODEL_CFG) or not os.path.exists(MODEL_WEIGHTS):
    raise FileNotFoundError("❌ YOLO model files not found! Check paths.")

net = cv2.dnn.readNetFromDarknet(MODEL_CFG, MODEL_WEIGHTS)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
print("[INFO] YOLOv4-tiny model loaded successfully ✅")

with open(CLASSES_FILE) as f:
    CLASSES = [c.strip() for c in f]

# ==================== Flask App ====================
app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
  <head>
    <title>YOLOv4-Tiny Object Detection</title>
  </head>
  <body style="text-align:center; font-family:Arial">
    <h2>YOLOv4-Tiny Object Detection</h2>
    <form method="POST">
      <button type="submit" style="font-size:20px; padding:10px 20px;">📸 Capture Image</button>
    </form>
    {% if img %}
      <h3>Detected Image:</h3>
      <img src="/output" style="max-width:90%; border:2px solid #333;">
    {% endif %}
  </body>
</html>
"""

# ==================== Helper Functions ====================
def adjust_camera_exposure():
    """Auto-adjust camera exposure for low light."""
    try:
        subprocess.run(["v4l2-ctl", "-d", f"/dev/video{CAMERA_DEVICE}", "--set-ctrl=exposure_auto=1"], check=False)
        subprocess.run(["v4l2-ctl", "-d", f"/dev/video{CAMERA_DEVICE}", "--set-ctrl=exposure_absolute=400"], check=False)
    except Exception:
        print("[WARN] Skipping exposure adjustment.")

def detect_objects(image):
    (H, W) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (320, 320), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(net.getUnconnectedOutLayersNames())

    boxes, confidences, classIDs = [], [], []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.4:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - width / 2)
                y = int(centerY - height / 2)
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
    if len(idxs) > 0:
        for i in idxs.flatten():
            x, y, w, h = boxes[i]
            label = f"{CLASSES[classIDs[i]]}: {confidences[i]:.2f}"
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, label, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

# ==================== Web Routes ====================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        adjust_camera_exposure()
        cap = cv2.VideoCapture(CAMERA_DEVICE, cv2.CAP_V4L2)
        cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        time.sleep(1.2)
        for _ in range(3): cap.read()

        ret, frame = cap.read()
        cap.release()

        if not ret:
            return "❌ Failed to capture image from camera."

        frame = cv2.convertScaleAbs(frame, alpha=1.3, beta=35)
        output = detect_objects(frame)
        cv2.imwrite(OUTPUT_IMAGE, output)
        print("[INFO] Detection complete:", OUTPUT_IMAGE)

        return HTML_PAGE.replace("{% if img %}", "").replace("{% endif %}", "").replace("/output", "/output")
    else:
        return HTML_PAGE.replace("{% if img %}", "").replace("{% endif %}", "")

@app.route("/output")
def output_image():
    if os.path.exists(OUTPUT_IMAGE):
        return send_file(OUTPUT_IMAGE, mimetype='image/jpeg')
    return "❌ No detected image yet."

if __name__ == "__main__":
    print("[INFO] Starting Flask server at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, threaded=True)
```

---

## 🔹 6. Run the Application

```bash
cd /root/models_V4
python3 obj1.py
```

Then, open a browser on your PC connected to the same network:

```cpp
http://<board-ip>:5000
```

Click 📸 **Capture Image** →  
The system captures one frame, detects objects, and displays the result instantly.

---

## 🔹 7. Performance Results

| Parameter | Before Optimization | After Optimization |
|-----------|--------------------|--------------------|
| Model | YOLOv4-Tiny (416×416) | YOLOv4-Tiny (320×320) |
| Avg Inference Time | ~30 sec | ~5 sec |
| Accuracy | High | Slightly reduced |
| Framework | OpenCV DNN | OpenCV DNN |
| Camera Format | MJPG | MJPG |
| Board | Buildroot Embedded Linux | Buildroot Embedded Linux |

---

## 🔹 8. Output

✅ Image brightness is auto-corrected using camera exposure + software gain.

✅ Each button click captures one frame, eliminating video latency.

✅ The processed image is displayed immediately on the web interface.

<p align="center">
  <img src="https://github.com/Senbagaseelan18/VLSI-Design-Contest/blob/main/Object%20Detection-YOLOv4-Tiny/Images/out.png" width="1000" alt="YOLOv4-Tiny Object Detection">
</p>

<p align="center">
  <img src="https://github.com/Senbagaseelan18/VLSI-Design-Contest/blob/main/Object%20Detection-YOLOv4-Tiny/Images/out1.png" width="1000" alt="YOLOv4-Tiny Object Detection">
</p>


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

**© 2025 VLSI Design Contest – YOLOv4-Tiny Object Detection Project**  
**Developed on Buildroot Linux using PolarFire® SoC Icicle Kit**

<br><br>

<img src="https://img.shields.io/badge/Setup_Status-Completed-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Detection-Active-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/Performance-Optimized-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Inference-Verified-orange?style=for-the-badge" />

</div>
