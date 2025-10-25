<div align="center">

  <h1>🛠️ VLSI-Design-Contest — EdgeSight Project</h1>
  
  <p>
    This repository documents the design and implementation of the  
    <b>EdgeSight</b> project: an FPGA-accelerated AI assistive device for the visually impaired,  
    built using the <b>Microchip PolarFire® SoC Icicle Kit</b>.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
    <img src="./Tool Installation & Setup Guide/Images/mic.png" width="200" alt="Microchip Technology logo">
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Project-EdgeSight-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Vision_&_Navigation-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Updating-orange?style=for-the-badge" />

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

> ⚠️ This is a **live, updating repository**. We will continuously update it with design files, simulation results, FPGA bitstreams, and firmware as the project progresses.

---

## 2. Completed Work

So far, the following milestones have been completed:

1. **Tool Installation & Setup Guide**  
   - Installed and configured **Libero® SoC Design Suite 2025.01**  
   - Installed **SoftConsole IDE 2024.2**  
   - License configuration and environment setup for both tools  

2. **Project Idea & Design Documentation**  
   - Detailed abstract and implementation plan for **EdgeSight**  
   - Block diagrams, vision, audio, navigation, and AI integration concepts  
   - References and related research documentation  

3. **Links to Completed Directories**  
   - [Tool Installation & Setup Guide](./Tool%20Installation%20&%20Setup%20Guide)  
   - [Project Idea & Documentation](./Project%20Idea)  

---

## 3. Current Work

We are currently focused on **booting the PolarFire® SoC Icicle Kit** with the latest Linux BSP image.  
This will provide a foundation for running the RISC-V firmware, integrating FPGA-accelerated AI models, and testing the EdgeSight system on the actual hardware.

- Linux BSP download and preparation  
- SD card flashing and board verification  
- Initial boot and hardware peripheral checks  

---

## 4. Access Project Directories

Click the links below to explore the completed sections of the repository:

- 📂 [Tool Installation & Setup Guide](./Tool%20Installation%20&%20Setup%20Guide)  
- 📂 [Project Idea & Documentation](./Project%20Idea)  
- 📂 [Boot Image Installation](./Boot%20Image%20Installation)  

---

## Project directories (quick links)

Below are the main project directories with one-line descriptions and quick links so contributors and reviewers can jump to what they need.

- 📁 [Boot Image Installation](./Boot%20Image%20Installation) — Step‑by‑step instructions and images to flash the Linux BSP and boot the PolarFire® SoC Icicle Kit.
- 🌐 [Internet_Connection](./Internet_Connection) — Network configuration, DHCP/static IP examples, and troubleshooting tips for connecting the board to your laptop or network.
- 💡 [LED_Blinking](./LED_Blinking) — Example code, images and short videos demonstrating LED blink patterns and simple firmware examples.
- 🧭 [Project Idea](./Project%20Idea) — Design documents, block diagrams, objectives and planned milestones for the EdgeSight project.
- 🖥️ [Web-based_led_control](./Web-based_led_control) — Flask web UI demo for controlling board LEDs over Ethernet; includes server code and HTML template.

---

### Quick status badges

<div>
  <img src="https://img.shields.io/badge/Boot-Image_OK-brightgreen" alt="boot" />
  <img src="https://img.shields.io/badge/Network-Docs_ready-blue" alt="network" />
  <img src="https://img.shields.io/badge/LED-Demos_present-orange" alt="leds" />
  <img src="https://img.shields.io/badge/Web_UI-ready-green" alt="webui" />
</div>

---

---

## 5. Summary

This repository consolidates all design, development, and documentation efforts for the **EdgeSight AI Assistive Device**.  
It serves as a **central reference** for tool setup, project ideas, FPGA and RISC-V co-design, and system integration.  

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

---

<div align="center">

**© 2025 VLSI Design Contest – EdgeSight Project Team**  
**Powered by Microchip PolarFire® SoC Technology**

</div>

---

## 🎯 Recent additions (summary)

The following project folders were added to the repository and are available under the repository root. I have *not* changed the content above — this is an additive summary to make the new material easier to find:

- `Boot Image Installation/` — Instructions and resources to flash the Linux BSP image and boot the PolarFire® SoC Icicle Kit.
- `Internet_Connection/` — Network setup and troubleshooting notes so the board can be accessed from your laptop/network.
- `LED_Blinking/` — Example files and media showing LED blinking demos and sample code.
- `Project Idea/` — Design concept, block diagrams and project planning documents for the EdgeSight project.
- `Web-based_led_control/` — A web interface demo (Flask + templates) for controlling board LEDs over the network. See the README inside that folder for full instructions and example code.

If you want, I can also:
- Add links to these directories into the Table of Contents at the top (keeping the original sections intact), or
- Create a short index file that lists each new directory with one-line descriptions and links.

Tell me which option you prefer and I will update the README accordingly.
