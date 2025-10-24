<div align="center">

  <h1>🧰 Tool Installation & Setup Guide</h1>
  
  <p>
    This section provides a complete guide for installing and configuring  
    the development tools required to work with the  
    <b>Microchip PolarFire® SoC Icicle Kit</b> used in the  
    <b>EdgeSight – AI-Powered Assistive Vision System</b> project.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/en/9/91/Microchip_Technology_logo.svg" width="200"/>
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Microchip-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FPGA-Libero_SoC_2025.01-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RISC–V-SoftConsole_2024.2-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-EdgeSight_Project-darkgreen?style=for-the-badge" />
</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **About Libero® SoC Design Suite** | [Jump to Section](#1-about-liberor-soc-design-suite) |
| 2 | **Libero® SoC Installation & License Setup** | [Jump to Section](#2-liberor-soc-installation--license-setup) |
| 3 | **About SoftConsole IDE** | [Jump to Section](#3-about-softconsole-ide) |
| 4 | **SoftConsole Installation & Setup** | [Jump to Section](#4-softconsole-installation--setup) |

---

## 🧩 1. About Libero® SoC Design Suite

**Libero® SoC Design Suite** is Microchip’s complete FPGA design environment that enables the design, synthesis, simulation, and programming of FPGAs such as the **PolarFire® SoC Icicle Kit**.  
It is the core tool used for developing the **FPGA hardware logic**, including custom accelerators, peripheral interfaces, and RTL design.

### 🔹 Key Features
- SmartDesign graphical system integration environment  
- Supports **VHDL**, **Verilog**, and **mixed-language** designs  
- Built-in **simulation**, **timing analysis**, and **device programming** tools  
- Seamless integration with **SoftConsole IDE** for co-design  
- Generates bitstream files for **PolarFire® SoC FPGA**  
- Ideal for **AI/ML acceleration**, **vision**, and **motor control** applications  

### 🔹 Official Resources
- 🔗 [Libero SoC Download Page](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions#downloads)  
- 🔗 [Microchip License Portal](https://www.microchipdirect.com/fpga-software-products)

---

## ⚙️ 2. Libero® SoC Installation & License Setup

### 🪜 Step 1: Download the Tool
1. Go to the official download page:  
   👉 [Libero SoC Design Suite 2025.01](https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions#downloads)
2. Download the correct version for your OS (Windows/Linux).  
3. Extract the downloaded archive and begin installation.  

---

### 🪜 Step 2: Obtain the License
1. Navigate to:  
   👉 [Microchip License Portal](https://www.microchipdirect.com/fpga-software-products)
2. Select **Libero Silver 1-Year DiskID NL License**.  
3. When prompted, enter your **Disk ID** (unique to your system).

#### 🧾 To Find Disk ID (Windows)
Open **Command Prompt** and run:
```bash
vol C:
