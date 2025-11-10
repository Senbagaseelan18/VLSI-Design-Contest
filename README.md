<div align="center">

# 🛠️ VLSI-Design-Contest — EdgeSight Project

This repository documents the design and implementation of the **EdgeSight** project: an FPGA-accelerated AI assistive device for the visually impaired, built using the **Microchip PolarFire® SoC Icicle Kit**.

<a href="https://www.microchip.com/" target="_blank">
  <img src="./Tool Installation & Setup Guide/Images/mic.png" width="200" alt="Microchip Technology logo">
</a>

<br><br>

![Project](https://img.shields.io/badge/Project-EdgeSight-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-PolarFire®_SoC-red?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Vision_&_Navigation-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **About This Repository** | [Jump to Section](#1-about-this-repository) |
| 2 | **Completed Work** | [Jump to Section](#2-completed-work) |
| 3 | **Current Work** | [Jump to Section](#3-current-work) |
| 4 | **Access Project Directories** | [Jump to Section](#4-access-project-directories) |
| 5 | **Summary** | [Jump to Section](#5-summary) |
| 6 | **Contributors** | [Jump to Section](#6-contributors) |
| 7 | **Acknowledgement** | [Jump to Section](#7-acknowledgement) |

---

## 1. About This Repository

This repository serves as the central hub for the **EdgeSight** project for the **39th International Conference on VLSI Design**.  
It is intended to document the complete workflow for developing an FPGA-accelerated AI assistive device, including:

- Tool installation and setup  
- FPGA design using **Libero® SoC Design Suite**  
- RISC-V firmware development using **SoftConsole IDE**  
- Project idea, design documents, and implementation strategy  
- Booting and running Linux BSP on the PolarFire® SoC Icicle Kit  
- Camera integration and live video streaming
- AI-powered object detection using YOLOv4-Tiny
- Web-based control interfaces

> ⚠️ This is a **live, updating repository**. We will continuously update it with design files, simulation results, FPGA bitstreams, and firmware as the project progresses.

---

## 2. Completed Work

The following milestones have been successfully completed:

### ✅ Development Tools & Environment
1. **Tool Installation & Setup Guide**  
   - Installed and configured **Libero® SoC Design Suite 2025.01**  
   - Installed **SoftConsole IDE 2024.2**  
   - License configuration and environment setup for both tools  

### ✅ Operating System & Boot Configuration
2. **Boot Image Installation**  
   - Linux BSP boot image with prebuilt filesystem and drivers
   - Board boot verification and peripheral checks

3. **Buildroot OS Building**  
   - Complete build system for custom Linux images
   - Microchip Buildroot External extension integration

4. **Yocto OS Booting**  
   - Microchip Yocto Linux BSP implementation
   - Alternative OS configuration and deployment

### ✅ Hardware Integration & Testing
5. **Internet Connectivity**  
   - Ethernet configuration via Windows laptop
   - Network access for package updates and remote repositories

6. **LED Control Systems**  
   - Basic LED blinking demonstrations
   - Web-based LED control interface using Flask

### ✅ Vision & AI Implementation
7. **USB Camera Setup**  
   - UVC-compliant camera integration
   - Camera access configuration in Buildroot Linux

8. **Live USB Camera Streaming**  
   - Real-time video streaming without ffmpeg
   - Flask web interface for live feed viewing

9. **Object Detection System**  
   - YOLOv4-Tiny implementation with OpenCV DNN
   - Single-image detection with web interface
   - Embedded system optimization

### ✅ Documentation
10. **Project Idea & Design Documentation**  
    - Detailed abstract and implementation plan
    - Block diagrams and system architecture
    - AI integration concepts and references

---

## 3. Current Work

We are currently focused on:

- Optimizing AI model performance on FPGA hardware
- Integrating real-time object detection with audio feedback
- Developing navigation assistance algorithms
- Testing and refining the complete EdgeSight system
- Performance benchmarking and power optimization

---

## 4. Access Project Directories

Click the links below to explore the project sections:

### 🔧 Development Tools
- 📂 [Tool Installation & Setup Guide](./Tool%20Installation%20&%20Setup%20Guide) — Complete guide for Libero® SoC and SoftConsole IDE installation and configuration

### 💡 Project Planning & Design
- 📂 [Project Idea](./Project%20Idea) — Design documents, block diagrams, objectives and implementation strategy for EdgeSight AI assistive device

### 🖥️ Operating Systems & Boot
- 📂 [Boot Image Installation](./Boot%20Image%20Installation) — Latest Linux BSP boot image with prebuilt filesystem, drivers, and kernel for PolarFire® SoC
- 📂 [Buildroot-OS-Building](./Buildroot-OS-Building) — Complete guide to build custom bootable Linux images using Microchip Buildroot External
- 📂 [Yocto_OS_Booting](./Yocto_OS_Booting) — Instructions to boot the board using Microchip's Yocto Linux BSP

### 🌐 Networking & Connectivity
- 📂 [Internet_Connection](./Internet_Connection) — Step-by-step Ethernet connectivity setup via Windows laptop for network access

### 💡 Hardware Control & Testing
- 📂 [LED_Blinking](./LED_Blinking) — Basic LED control demonstrations on Yocto Linux
- 📂 [Web-based_led_control](./Web-based_led_control) — Flask-based web interface for controlling on-board LEDs over Ethernet

### 📷 Vision System & AI
- 📂 [USB-Camera-Setup](./USB-Camer-Setup) — Complete UVC-compliant USB camera setup and configuration on Buildroot Linux
- 📂 [Live USB Camera Stream](./Live%20USB%20Camera%20Stream) — Real-time video streaming setup using Flask web interface (no ffmpeg required)
- 📂 [Object Detection-YOLOv4-Tiny](./Object%20Detection-YOLOv4-Tiny) — Single-image object detection using YOLOv4-Tiny with OpenCV DNN and Flask interface

---

## Project Directories (Quick Reference)

Below is a quick reference table with all project directories:

| 📁 Directory | 📝 Description | 🔗 Link |
|-------------|----------------|---------|
| **Tool Installation & Setup Guide** | Development tools installation and configuration | [View](./Tool%20Installation%20&%20Setup%20Guide) |
| **Project Idea** | Design documents and system architecture | [View](./Project%20Idea) |
| **Boot Image Installation** | Linux BSP boot image and setup | [View](./Boot%20Image%20Installation) |
| **Buildroot-OS-Building** | Custom Linux image building guide | [View](./Buildroot-OS-Building) |
| **Yocto_OS_Booting** | Yocto Linux BSP boot instructions | [View](./Yocto_OS_Booting) |
| **Internet_Connection** | Ethernet connectivity configuration | [View](./Internet_Connection) |
| **LED_Blinking** | Basic LED control examples | [View](./LED_Blinking) |
| **Web-based_led_control** | Web interface for LED control | [View](./Web-based_led_control) |
| **USB-Camera-Setup** | USB camera integration guide | [View](./USB-Camer-Setup) |
| **Live USB Camera Stream** | Real-time video streaming system | [View](./Live%20USB%20Camera%20Stream) |
| **Object Detection-YOLOv4-Tiny** | AI-powered object detection | [View](./Object%20Detection-YOLOv4-Tiny) |

---

### Quick Status Badges

<div>
  <img src="https://img.shields.io/badge/Boot-Image_OK-brightgreen" alt="boot" />
  <img src="https://img.shields.io/badge/Buildroot-Configured-blue" alt="buildroot" />
  <img src="https://img.shields.io/badge/Yocto-Booting-green" alt="yocto" />
  <img src="https://img.shields.io/badge/Network-Connected-brightgreen" alt="network" />
  <img src="https://img.shields.io/badge/LED-Control_Ready-orange" alt="leds" />
  <img src="https://img.shields.io/badge/USB_Camera-Configured-blue" alt="camera" />
  <img src="https://img.shields.io/badge/Live_Stream-Active-green" alt="stream" />
  <img src="https://img.shields.io/badge/Object_Detection-YOLOv4_Tiny-red" alt="ai" />
  <img src="https://img.shields.io/badge/Web_UI-Ready-brightgreen" alt="webui" />
</div>

---

## 5. Summary

This repository consolidates all design, development, and documentation efforts for the **EdgeSight AI Assistive Device**.  
It serves as a **central reference** for:

- 🛠️ **Development Environment Setup** — Tool installation and configuration
- 🖥️ **Operating System Deployment** — Multiple Linux distributions (BSP, Buildroot, Yocto)
- 🌐 **Network Integration** — Ethernet connectivity and web interfaces
- 💡 **Hardware Control** — LED demonstrations and peripheral testing
- 📷 **Vision System** — USB camera setup and live streaming
- 🤖 **AI Implementation** — Real-time object detection using YOLOv4-Tiny
- 📚 **Comprehensive Documentation** — Step-by-step guides for every component

As the project progresses, this repository will be **continuously updated** with new developments, implementation files, and results from the PolarFire® SoC Icicle Kit.

---

## 6. Contributors

| Name | GitHub Profile |
|------|----------------|
| **Senbagaseelan V** | [@Senbagaseelan18](https://github.com/Senbagaseelan18) |
| **Praveen R** | [@PRAVEENRAMU14](https://github.com/PRAVEENRAMU14) |
| **Ragul T** | [@Ragul-2005](https://github.com/Ragul-2005) |
| **Tharun Babu V** | [@TharunBabu-05](https://github.com/TharunBabu-05) |

---

## 7. Acknowledgement

We sincerely thank **Microchip Technology Inc.** for providing the **PolarFire® SoC Icicle Kit**, **Libero® SoC**, and **SoftConsole IDE**.  
Their platform and resources have been instrumental in enabling students to innovate and implement **FPGA and AI solutions** in the VLSI Design Contest.

Special thanks to the open-source community for tools and libraries including:
- **Buildroot** and **Yocto Project** for embedded Linux development
- **OpenCV** and **YOLOv4** for computer vision capabilities
- **Flask** for rapid web interface development

---

<div align="center">

**© 2025 VLSI Design Contest – EdgeSight Project Team**  
**Powered by Microchip PolarFire® SoC Technology**

### 🌟 Star this repository if you find it helpful!

</div>

---
