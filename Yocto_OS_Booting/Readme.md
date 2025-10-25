<div align="center">

  <h1>💻 PolarFire SoC Icicle Kit Linux Boot Guide</h1>
  
  <p>
    Step-by-step instructions to boot the <b>PolarFire® SoC Icicle Kit</b>  
    using Microchip’s Yocto Linux BSP for the  
    <b>EdgeSight – AI-Powered Assistive Vision System</b> project.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
  <img src="./Images/mic.png" width="200" alt="Microchip Technology logo">
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Microchip-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linux-Yocto_BSP-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-EdgeSight_Project-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flashing-BalenaEtcher-orange?style=for-the-badge" />
</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Overview** | [Jump to Section](#-1-overview) |
| 2 | **Installed OS** | [Jump to Section](#-2-installed-os) |
| 3 | **Flashing OS with BalenaEtcher** | [Jump to Section](#-3-flashing-os-with-balenaetcher) |
| 4 | **Booting & Logging into Linux** | [Jump to Section](#-4-booting--logging-into-linux) |
| 5 | **Summary & Notes** | [Jump to Section](#-5-summary--notes) |

---

## 🧩 1. Overview

This guide demonstrates:

- Flashing the PolarFire SoC Icicle Kit Linux image using **BalenaEtcher**.  
- Booting the board and logging in via UART.  
- Verifying Linux system directories.

---

## 🧩 2. Installed OS

We used the prebuilt Yocto Linux image:

```text
mchp-base-image-mpfs-icicle-kit.rootfs-20250725101827.wic
```
- PolarFire SoC Yocto BSP version: v2025.07  
- Boots Linux directly without updates.

---

## 🧩 3. Flashing OS with BalenaEtcher

### Step 1: Download and Install BalenaEtcher

- Visit [https://www.balena.io/etcher/](https://www.balena.io/etcher/)  
- Download the appropriate version for your OS (Windows, Linux, or macOS) and install it.

### Step 2: Select OS Image

- Open BalenaEtcher.  
- Click **“Flash from file”** and select:  

```text
mchp-base-image-mpfs-icicle-kit.rootfs-20250725101827.wic
```

### Step 3: Select Target Device

- Insert your SD card or eMMC into the PC.  
- Click **“Select Target”** and choose the correct device.

### Step 4: Flash the Image

- Click **“Flash!”**  
- Wait for the flashing and validation process to complete.

  <p align="center">
    <img width="996" height="627" alt="image" src="https://github.com/user-attachments/assets/4402f095-d993-4c7c-a554-3f9478cdb394" />
  </p>


### Step 5: Insert SD/eMMC into Icicle Kit

- Safely eject the SD card or eMMC from your PC.  
- Insert it into the PolarFire SoC Icicle Kit.

> ⚠️ Ensure you select the correct target device in BalenaEtcher to avoid data loss.

---

## 🧩 4. Booting & Logging into Linux

### Step 1: Power On

- Power on the Icicle Kit after inserting the SD/eMMC.

  <p align="center">
    <img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/2793e108-6ed4-40e6-87d3-e3ac5fe7f8d7" />
</p>

### Step 2: Connect via Putty

- Connect the board to your PC using a UART/serial interface.  
- Serial settings:  
- Baud rate: 115200  
- Data bits: 8  
- Stop bit: 1  
- No parity, no flow control

  <p align="center">
    <img width="595" height="538" alt="image" src="https://github.com/user-attachments/assets/60ee8847-f3c1-432b-b5cd-8a270d48914b" /></p>


### Step 3: Login as Root

```text
mpfs-icicle-kit login: root
```

### Step 4: Verify Linux Directories

```bash
ls /
```

- ✅ Successful boot confirmed by root prompt:

  ```text
   root@mpfs-icicle-kit:~#
  ```

<p align="center">
  <img width="826" height="515" alt="image" src="https://github.com/user-attachments/assets/3fdccc49-aa1c-47d8-a874-1883c9d120e9" />
</p>

 ### 🧩 5. Summary & Notes

- The Yocto Linux BSP provides root access without a password.
- Flashing with BalenaEtcher ensures a reliable write of the .wic image to SD/eMMC.
- Boot process verified via UART console.
- Directories confirmed for Linux environment setup.
- Ready for next steps: LED control and firmware development.

<div align="center"> <img src="https://img.shields.io/badge/Boot_Status-Completed-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/Board-PolarFire®_SoC_Icicle_Kit-red?style=for-the-badge" /> <img src="https://img.shields.io/badge/Platform-EdgeSight_AI_Assistive_Device-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Flashing-BalenaEtcher-orange?style=for-the-badge" /> </div>

## 👩‍💻 Contributors

| Name | GitHub Profile |
|------|----------------|
| **Senbagaseelan V** | [@Senbagaseelan18](https://github.com/Senbagaseelan18) |
| **Praveen R** | [@PRAVEENRAMU14](https://github.com/PRAVEENRAMU14) |
| **Ragul T** | [@Ragul-2005](https://github.com/Ragul-2005) |
| **Tharun Babu V** | [@TharunBabu-05](https://github.com/TharunBabu-05) |


<div align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Microchip_logo.svg" width="160" alt="Microchip Logo" />

© 2025 VLSI Design Contest – EdgeSight Project Team
Powered by Microchip PolarFire® SoC Technology

</div> ```

