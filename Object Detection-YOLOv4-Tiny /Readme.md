<div align="center">

  <h1>🟢 Object Detection using YOLOv4-Tiny – Flask Web Interface</h1>
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
It is optimized to work **without PyTorch or ONNX Runtime**, relying only on **OpenCV’s DNN backend** for inference.  
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
