<div align="center">

  <h1>🟢 Object Detection using YOLOv4-Tiny – Flask Web Interface</h1>
  <p>
  This repository demonstrates a **single-frame object detection system** implemented on a **Linux-based embedded board** using **YOLOv4-Tiny** with the **OpenCV DNN module** and **Flask web interface**.  
  The system captures a single image from a **USB camera**, performs **real-time object detection**, and displays the output instantly on a webpage.
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
| 1 | **Objective** | [Jump to Section](#-1-objective) |
| 2 | **System Configuration** | [Jump to Section](#-2-system-configuration) |
| 3 | **Implementation Steps** | [Jump to Section](#-3-implementation-steps) |
| 4 | **Buildroot Menuconfig Settings** | [Jump to Section](#-4-buildroot-menuconfig-settings) |
| 5 | **Execution Steps** | [Jump to Section](#-5-execution-steps) |
| 6 | **Result** | [Jump to Section](#-6-result) |
| 7 | **Repository Structure** | [Jump to Section](#-7-repository-structure) |
| 8 | **Contributors** | [Jump to Section](#-8-contributors) |

---

## 🔹 1. Objective
This project enables **real-time object detection** using **YOLOv4-Tiny** on an embedded Linux system.  
It is optimized to work **without PyTorch or ONNX Runtime**, relying only on **OpenCV's DNN backend** for inference.  
The application captures a **single high-quality image** from a **USB camera** and processes it using **YOLOv4-Tiny**, displaying results through a **Flask web interface**.

---

## 🔹 2. System Configuration

| Parameter | Description |
|------------|-------------|
| **Board** | Microchip PolarFire SoC Icicle Kit |
| **OS** | Buildroot Linux (custom image) |
| **Python Version** | 3.10 |
| **Framework** | Flask |
| **Vision Library** | OpenCV 4.10 |
| **Model Used** | YOLOv4-Tiny |
| **Detection Mode** | Single Frame |
| **Interface** | USB Camera (V4L2 MJPEG) |

---

## 🔹 3. Implementation Steps

### Step 1️⃣ – Clone the Repository
```bash
git clone https://github.com/<your-username>/YOLOv4-Tiny-ObjectDetection-WebApp.git
cd YOLOv4-Tiny-ObjectDetection-WebApp
```

### Step 2️⃣ – Download Model Files
```bash
wget --no-check-certificate https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
wget --no-check-certificate https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
wget --no-check-certificate https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
```

Place them inside:

```bash
/root/models_V4/
```

### Step 3️⃣ – Verify OpenCV Modules
```bash
python3 -c "import cv2; print(cv2.getBuildInformation())"
```
Ensure `dnn`, `videoio`, `imgproc`, and `highgui` are listed as enabled.

---

## 🔹 4. Buildroot Menuconfig Settings
This section details everything you must enable inside Buildroot to support:

- Python 3
- Flask framework
- OpenCV (DNN + video + GStreamer)
- USB Camera
- HTTPS downloads

### ⚙️ Step 1 – Python Packages
In Buildroot:

```css
Target packages  --->
    Interpreter languages and scripting  --->
        [*] python3
        [*] python3-pip
        [*] python3-numpy
        [*] python3-requests
        [*] python3-pillow
        [*] python3-flask
        [*] python3-scapy
        [*] python3-schedule
        [*] python3-setuptools
```

✅ **Explanation:**

| Package | Purpose |
|---------|---------|
| python3 | Core Python interpreter |
| python3-pip | Install any additional modules |
| python3-flask | Web framework for interface |
| python3-numpy | Needed for OpenCV DNN operations |
| python3-pillow | Image handling |
| python3-requests | HTTP communication (optional for API) |
| python3-setuptools | Build dependencies for Python libs |

### ⚙️ Step 2 – OpenCV Configuration
Navigate to:

```lua
Target packages --->
    Graphic libraries and applications --->
        opencv4 --->
```

Then enable:

```css
--- opencv4
    [*] dnn
    [*] features2d
    [*] highgui
    [*] imgcodecs
    [*] imgproc
    [*] ml
    [*] objdetect
    [*] shape
    [*] stitching
    [*] ts
    [*] video
    [*] videoio
    [*] gstreamer-1.x
    [*] ffmpeg
    [*] jpeg
    [*] png
    [*] tiff
    [*] v4l
    [*] webp
    [*] install extra data
```

✅ **Explanation:**

| Option | Purpose |
|--------|---------|
| dnn | Enables YOLO inference through OpenCV |
| videoio | Handles camera input |
| gstreamer / ffmpeg | Stream and decode MJPEG frames |
| jpeg, png, tiff | Enables image file encoding |
| v4l | USB camera capture support |

### ⚙️ Step 3 – USB & Networking Support
```css
Hardware handling --->
    [*] v4l2-utils
Networking applications --->
    [*] ca-certificates
    [*] wget
```

✅ **Explanation:**

- **v4l2-utils:** Controls camera parameters (exposure, format)
- **ca-certificates:** Required for HTTPS file downloads
- **wget:** For model file retrieval from GitHub

---

## 🔹 5. Execution Steps

### ▶️ Step 1 – Transfer Files
```bash
scp -r YOLOv4-Tiny-ObjectDetection-WebApp root@<board-ip>:/root/
```

### ▶️ Step 2 – Run Flask Application
```bash
cd /root/models_V4
python3 obj1_fast.py
```

### ▶️ Step 3 – Access Web Interface
Open in browser:

```cpp
http://<board-ip>:5000
```

Click 📸 **Capture Image** to trigger detection and view results.

---

## 🔹 6. Result
✅ Captures high-quality still image via MJPEG  
✅ Runs YOLOv4-Tiny DNN model in OpenCV backend  
✅ Displays bounding boxes on web interface  
✅ Achieves detection time ~5–7 seconds (CPU only)

---

## 🔹 7. Repository Structure
```bash
YOLOv4-Tiny-ObjectDetection-WebApp/
├── obj1_fast.py               # Flask application script
├── yolov4-tiny.cfg            # YOLOv4-Tiny configuration
├── yolov4-tiny.weights        # Pretrained YOLOv4-Tiny model
├── coco.names                 # Object label file
└── README.md                  # Documentation
```

---

## 🔹 8. Contributors

| 👤 Name | 🏢 Organization | 💼 Role |
|---------|----------------|---------|
| Senbagaseelan V | Embedded Vision Research | Project Developer |
| ChatGPT (OpenAI) | Technical Assistant | Architecture & Optimization |

---

<div align="center">

⚡ **YOLOv4-Tiny | Flask | OpenCV DNN | Buildroot Linux**  
🎯 **Optimized for Microchip PolarFire SoC Icicle Kit**  
📷 **USB Camera Interface | 🧠 Onboard CPU Inference**

</div>
