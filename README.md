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
```

You’ll get an output like:

```bash 
Volume in drive C is OS
Volume Serial Number is XXXX-XXXX
```

The **Volume Serial Number** is your Disk ID.

4. After submission, **Microchip** will send you a License.dat file.

### 🪜 Step 3: Save the License File

1. Create a new folder in your C drive:
   ```bash
   C:\flexlm
    ```
2. Copy the provided **License.dat** file into this folder.

### 🪜 Step 4: Set Environment Variable

1. Open **System Properties → Advanced System Settings → Environment Variables**.  
   _(Shortcut: press `Windows + W` → search “Environment Variables”)_

2. Under **System Variables**:

   - If `LM_LICENSE_FILE` exists → **Edit** → add  
     ```bash
     C:\flexlm\License.dat
     ```
   - If not → **Create New Variable**  
     ```bash
     Name:  LM_LICENSE_FILE
     Value: C:\flexlm\License.dat
     ```

> ⚠️ Ensure path and folder names match exactly (case-sensitive).

3. Click **OK** to apply and close all dialogs.

---

### 🪜 Step 5: Verify Installation

- Launch **Libero SoC Design Suite**.  
- Navigate to **Help → Manage License**.  
- Verify that **Libero Silver License** is detected.

✅ **Libero SoC 2025.01** is now fully installed and ready for FPGA design.

---

## 💻 3. About SoftConsole IDE

**SoftConsole** is Microchip’s **Eclipse-based Integrated Development Environment (IDE)** for software development on **RISC-V** and **ARM-based SoCs**.  
For the **PolarFire® SoC Icicle Kit**, SoftConsole is used to develop and debug C/C++ firmware that runs on the RISC-V cores, coordinating with FPGA logic designed in Libero.

### 🔹 Key Features

- Supports **bare-metal** and **Linux-based** RISC-V applications  
- Integrated **GCC toolchain** and **debugger**  
- Prebuilt **Board Support Packages (BSPs)** for PolarFire SoC  
- Seamless **hardware-software co-design** with Libero  
- Ideal for real-time control, data acquisition, and sensor processing tasks  

### 🔹 Official Resource

🔗 [SoftConsole IDE Download Page](https://www.microchip.com/en-us/tools-resources/develop/microchip-softconsole)

---

## ⚙️ 4. SoftConsole Installation & Setup

### 🪜 Step 1: Installation

1. Download **SoftConsole v2024.2 or newer** from the official Microchip page.  
2. Install or extract the package based on your OS.  
3. Launch the IDE and configure your workspace folder.

---

### 🪜 Step 2: Board Setup

1. Install the **PolarFire® SoC BSP (Board Support Package)** when prompted.  
2. Connect your **Icicle Kit** to the PC using USB.  
3. Open the terminal in **SoftConsole** to check UART communication.

---

### 🪜 Step 3: Verification

- Create a sample RISC-V “Hello World” project.  
- Build and program it using the **Debug** option.  
- Verify output on the serial console.

✅ **SoftConsole** is now ready for firmware development and debugging.

---

<div align="center">

<img src="https://img.shields.io/badge/Setup_Status-Completed-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/Tools-Libero_&_SoftConsole-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Board-PolarFire®_SoC_Icicle_Kit-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/Project-EdgeSight_AI_Assistive_Device-green?style=for-the-badge" />

</div>
