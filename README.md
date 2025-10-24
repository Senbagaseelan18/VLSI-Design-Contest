<div align="center">

  <h1>⚙️ PolarFire® SoC Icicle Kit — Tool Setup and Environment Configuration</h1>

  <p>
    This repository documents the setup and configuration process for the development environment  
    used in the <b>EdgeSight</b> project — a real-time AI-powered assistive vision system for  
    visually impaired individuals.  
  </p>

  <p>
    The project utilizes <b>Microchip Technology’s PolarFire® SoC FPGA</b>, combining RISC-V processors  
    with FPGA fabric for high-performance, low-power AI/ML processing at the edge.
  </p>

  <img src="https://img.shields.io/badge/Microchip-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RISC-V-Development-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FPGA-Libero_SoC-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Software-SoftConsole-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-EdgeSight_Project-darkgreen?style=for-the-badge" />

</div>

---

# 📘 Table of Contents  

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **About Libero® SoC Design Suite** | [Go to Section](#1-about-liberor-soc-design-suite) |
| 2 | **Libero® SoC Installation & License Setup** | [Go to Section](#2-liberor-soc-installation--license-setup) |
| 3 | **About SoftConsole IDE** | [Go to Section](#3-about-softconsole-ide) |
| 4 | **SoftConsole Installation & Setup** | [Go to Section](#4-softconsole-installation--setup) |

---

## 1️⃣ About Libero® SoC Design Suite

**Libero® SoC Design Suite** is Microchip’s comprehensive FPGA design environment, enabling users to design, simulate, and program PolarFire® and SmartFusion® FPGAs.  
It provides an integrated toolchain for RTL design, synthesis, implementation, timing analysis, simulation, and hardware programming.

### 🔹 Key Features
- SmartDesign graphical system integration environment  
- Supports **VHDL**, **Verilog**, and **mixed-language** projects  
- Built-in **simulation** and **timing analysis** tools  
- Tight integration with **SoftConsole IDE** for hardware-software co-design  
- Generates bitstream files for **PolarFire® SoC FPGA programming**  
- Ideal for projects involving **AI/ML acceleration**, **vision**, and **motor control**

### 🔹 Official Resources
- 🔗 [Libero SoC Downloads Page](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions#downloads)  
- 🔗 [Microchip License Portal](https://www.microchipdirect.com/fpga-software-products)  

---

## 2️⃣ Libero® SoC Installation & License Setup

### 🧩 Step 1: Download the Tool
1. Visit the official download page:  
   👉 [Libero SoC Design Suite 2025.01](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions#downloads)
2. Download the appropriate installer for your OS.  
3. Extract the downloaded archive and start the installation wizard.  

---

### 🧩 Step 2: Obtain the License
1. Go to:  
   👉 [Microchip License Portal](https://www.microchipdirect.com/fpga-software-products)
2. Select **Libero Silver 1 Year DiskID NL License**.  
3. The website will request your **Disk ID**.

#### 🔸 To get the Disk ID (Windows):
```bash
vol C:
