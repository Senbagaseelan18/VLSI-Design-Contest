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
  
