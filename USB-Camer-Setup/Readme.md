<div align="center">

  <h1>📸 USB Cam Recorder – Video Capture & Transfer System</h1>
 This documentation explains the complete <b>Camera Setup</b> and <b>Camera Access</b> process  
    for integrating a UVC-compliant USB Camera on an embedded Linux system built using  
    <b>Buildroot</b> for the <b>VLSID 2026 Design Contest</b>.
  </p>

  
  <a href="https://www.microchip.com/" target="_blank">
<img width="270" height="180" alt="image" src="https://github.com/user-attachments/assets/1d5e8b0d-e14c-4ee5-8a40-ab32b5b485f0" />
  </a>
  <br><br>
 <img src="https://img.shields.io/badge/Interface-USB_Camera-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Buildroot_Linux-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Video-MJPEG_1080p@30fps-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Project-VLSID_2026-red?style=for-the-badge" />

</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Objective** | [Jump to Section](#-1-objective) |
| 2 | **Requirements** | [Jump to Section](#-2-requirements) |
| 3 | **CAM SETUP** | [Jump to Section](#-3-cam-setup) |
| 4 | **Implementation Steps** | [Jump to Section](#-4-implementation-steps) |
| 5 | **Output & Verification** | [Jump to Section](#-5-output--verification) |
| 6 | **Observations & Results** | [Jump to Section](#-6-observations--results) |
| 7 | **Repository Structure** | [Jump to Section](#-7-repository-structure) |
| 8 | **Contributors** | [Jump to Section](#-8-contributors) |

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

# 🧰 3. CAM SETUP

This section focuses on enabling hardware and driver-level support for USB Camera integration in the **Buildroot-based Linux environment**.

---

## ⚙️ 1. Hardware Configuration

| Component | Setting / Description |
|------------|-----------------------|
| **USB Controller** | Dual-role OTG (On-The-Go) – USB 2.0 Compliant |
| **Jumpers** | Close **J15** and **J17** on Icicle Kit to enable USB Host mode |
| **Default Configuration** | J15 & J17 Open → acts as USB Device |
| **Important Note** | To reprogram eMMC → open J15 and J17 |

---

## 🧩 2. Buildroot Driver Enablement

To work with USB video devices, such as webcams, the following packages need to be included in the yocto or buildroot build systems.

```bash
yavta \
libuvc \
gstd \
gstreamer1.0-plugins-good \
v4l-utils \
```

## 📸 3. Accessing a Webcam

Use the below command to capture an image from a webcam
```bash
v4l2-ctl --device /dev/video0 --set-fmt-video=width=640,height=480,pixelformat=MJPG --stream-mmap=3 --stream-count=100 --stream-to=stream.vid
```

## ⚠️ 4. Known Issues
- 1.VBUS_ERROR in a_idle error.

A VBUS_ERROR occurs when you boot Linux and then connect a USB device (e.g a webcam) directly to J16. Solution: Rather than connecting the webcam directly, connect a powered hub to J16 on the Icicle Kit, and then connect the webcam to the hub. To connect high power USB device, its is better to use an externally powered USB hub in between the USB device and the Icicle Kit.

- 2. If a VBUS_ERROR is displayed and LEDs turns off, a board power cycle will be needed to get the USB port working.

---


## 🚀 4. Implementation Steps

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
ffmpeg -f mjpeg -i video.mjpg -c:v libx264 -preset fast -pix_fmt yuv420p video2.mp4
```

<b>✅ Converted file video.mp4 plays smoothly with correct frame rate.<b>


# 🖥️ 4. Output & Verification

Playback verified using:

- 🎥 VLC Media Player

- 🎞️ Windows Media Player

## 🖥️ Output & Verification


| 🧩 **Stage** | 📝 **Description** |
|--------------|--------------------|
| 🟢 **Camera Capturing** | The USB camera successfully captured live 1080p video using V4L2 commands. | 
| 🔴 **Video Recording** | Recorded ~10 seconds of MJPEG video and saved as `/root/video.mjpg` on the board. | 
| 🔵 **Playback Verification** | The converted `video.mp4` played smoothly on VLC/Windows Media Player with correct frame rate and brightness. | 

---

#🧠 6. Observations & Results

- ✅ Successful USB camera interface and detection

- ✅ Stable 1080p@30fps video recording

- ✅ Verified SCP-based file transfer to host

- ✅ Confirmed V4L2 + FFmpeg compatibility in Linux

- ✅ Smooth playback verified on multiple media players

---

# 📂 7. Repository Structure
```bash
usb-cam-recorder/
│
├── README.md
├── report/
│   └── CAMERA_RECORDING_AND_VIDEO_TRANSFER_REPORT.pdf
├── scripts/
│   ├── capture_video.sh
│   ├── transfer_video.sh
│   └── convert_video.sh
├── images/
│   ├── cam_capture.jpg
│   ├── video_recording.jpg
│   └── video_playback.jpg
└── LICENSE
```

# 👩‍💻 8. Contributors

| 👤 **Name** | 🌐 **GitHub Profile** |
|-------------|-----------------------|
| **Senbagaseelan V** | [@Senbagaseelan18](https://github.com/Senbagaseelan18) |
| **Praveen R** | [@PRAVEENRAMU14](https://github.com/PRAVEENRAMU14) |
| **Ragul T** | [@Ragul-2005](https://github.com/Ragul-2005) |
| **Tharun Babu V** | [@TharunBabu-05](https://github.com/TharunBabu-05) |

---

<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Microchip_logo.svg" width="160" alt="Microchip Logo" />

**© 2025 VLSI Design Contest – USB Cam Recorder Project**  
**Developed on Buildroot Linux using PolarFire® SoC Icicle Kit**

<br><br>

<img src="https://img.shields.io/badge/Setup_Status-Completed-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Recording-Working-green?style=for-the-badge" />
<img src="https://img.shields.io/badge/Transfer-Successful-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Playback-Verified-orange?style=for-the-badge" />

</div>

