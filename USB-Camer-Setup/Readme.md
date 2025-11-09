<div align="center">

  <h1>📸 USB Cam Recorder – Video Capture & Transfer System</h1>
  
  <p>
    This section documents the complete setup, implementation, and validation  
    of a <b>USB Camera Recording and Video Transfer Pipeline</b> developed for  
    embedded Linux environments in the <b>VLSID 2026 Design Contest</b>.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
    <img src="./images/mic.png" width="200" alt="Microchip Technology logo">
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Interface-USB_Camera-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Video-MJPEG_1080p@30fps-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Transfer-SCP_Protocol-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Linux_Embedded-darkred?style=for-the-badge" />
</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Objective** | [Jump to Section](#-1-objective) |
| 2 | **Requirements** | [Jump to Section](#-2-requirements) |
| 3 | **Implementation Steps** | [Jump to Section](#-3-implementation-steps) |
| 4 | **Output & Verification** | [Jump to Section](#-4-output--verification) |
| 5 | **Observations & Results** | [Jump to Section](#-5-observations--results) |
| 6 | **Repository Structure** | [Jump to Section](#-6-repository-structure) |
| 7 | **Contributors** | [Jump to Section](#-7-contributors) |

---


## 🧩 1. Objective

The primary objective of this work is to design and validate a **complete video capture and transfer system** using a **UVC-compliant USB camera** on an embedded Linux environment.  

The system performs:
- Real-time **MJPEG video recording**
- **Local storage** of captured video on the device filesystem
- Secure **video transfer to a remote system (Windows/Linux)** using SCP protocol
- Post-processing and **conversion to MP4 format** using FFmpeg

---

## ⚙️ 2. Requirements

### **Hardware**
- 🖥️ Embedded Linux Platform (e.g., SoC board with USB host)
- 📸 USB Camera (UVC Compliant)
- 💻 Windows / Linux PC (for SCP transfer & playback)

### **Software / Tools**
- `v4l2-ctl` (Video4Linux2 utilities)
- `FFmpeg` (video conversion)
- `scp` (file transfer)
- Linux with **V4L2** and **UVC camera support**

---

## 🚀 3. Implementation Steps

### 🧮 Step 1 – Detect the Camera
```bash
ls /dev/video*
```

### Output:
```
/dev/video0
```

## 🎞️ Step 2 – Check Supported Formats
```bash
v4l2-ctl --device=/dev/video0 --list-formats-ext
```

### Result:
```
MJPG: 1920x1080 @ 30fps
YUYV: 640x480 @ 30fps
```

## ⚙️ Step 3 – Set Video Format
```bash
v4l2-ctl -d /dev/video0 --set-fmt-video=width=1920,height=1080,pixelformat=MJPG
```

## ⏺️ Step 4 – Record Video (10 seconds)

```bash
v4l2-ctl -d /dev/video0 --stream-mmap --stream-count=300 --stream-to=/root/video.mjpg
```

### ✅ Output: 
```
video.mjpg created successfully
```

## 🔍 Step 5 – Verify Video File
```bash
ls -lh /root/video.mjpg
file /root/video.mjpg
```

### Output:

```
video.mjpg: Motion JPEG video data
```

## 💾 Step 6 – Transfer File via SCP
```bash
scp root@192.168.137.2:/root/video.mjpg .
```

<b>✅ File successfully transferred to the host system.</b>

## 🎬 Step 7 – Convert to MP4 (on PC)
```bash
ffmpeg -i video.mjpg -c:v libx264 -preset fast -crf 23 video.mp4
```

<b>✅ Converted file video.mp4 plays smoothly with correct frame rate.<b>


# 🖥️ 4. Output & Verification

Playback verified using:

-🎥 VLC Media Player

-🎞️ Windows Media Player

Stage	Description	Example
🟢 Camera Capture	Live USB feed captured	

🔴 Recording	1080p MJPEG recording	

🔵 Transfer & Playback	MP4 playback on PC	
🧠 5. Observations & Results

✅ Successful USB camera interface and detection

✅ Stable 1080p@30fps video recording

✅ Verified SCP-based file transfer to host

✅ Confirmed V4L2 + FFmpeg compatibility in Linux

✅ Smooth playback verified on multiple media players
