<div align="center">

  <h1>💡 PolarFire SoC Icicle Kit LED Control Guide</h1>
  
  <p>
    Step-by-step instructions to control the on-board LEDs on the  
    <b>PolarFire® SoC Icicle Kit</b> running Yocto Linux for the  
    <b>EdgeSight – AI-Powered Assistive Vision System</b> project.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
  <img src="./Images/mic.png" width="200" alt="Microchip Technology logo">
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Microchip-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linux-Yocto_BSP-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-EdgeSight_Project-darkgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Feature-LED_Control-yellow?style=for-the-badge" />
</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Overview** | [Jump to Section](#-1-overview) |
| 2 | **List Available LEDs** | [Jump to Section](#-2-list-available-leds) |
| 3 | **Single LED Control** | [Jump to Section](#-3-single-led-control) |
| 4 | **LED Blinking Patterns** | [Jump to Section](#-4-led-blinking-patterns) |
| 5 | **Push Button Controlled LED** | [Jump to Section](#-5-push-button-controlled-led) |
| 6 | **Save Scripts for Future Use** | [Jump to Section](#-6-save-scripts-for-future-use) |
| 7 | **Summary & Notes** | [Jump to Section](#-7-summary--notes) |
| 8 | **Contributors** | [Jump to Section](#-8-contributors) |

---

## 🧩 1. Overview

This guide demonstrates:

- How to check and control LEDs on the PolarFire SoC Icicle Kit.  
- How to create **continuous, sequential, and Knight Rider LED patterns**.  
- How to control LEDs using **push buttons**.  
- How to save scripts for reuse.

---

## 🧩 2. List Available LEDs

Check which LEDs are available:

```bash
ls /sys/class/leds
```

Expected output:

```bash
led1  led2  led3  led4
```

## 🧩 3. Single LED Control

Turn ON:
```bash
echo 1 > /sys/class/leds/led1/brightness
```
<p align="center"><img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/b12bcb16-128e-4afb-bead-1f874bb29c26" /></p>

Turn OFF:
```bash
echo 0 > /sys/class/leds/led1/brightness
```

<p align="center">
  <img width="972" height="598" alt="image" src="https://github.com/user-attachments/assets/ff9f4705-eb82-458a-a981-6f8e048259ce" />
</p>

## 🧩 4. LED Blinking Patterns
# 4.1 Continuous Blinking
```bash
while true; do
  echo 1 > /sys/class/leds/led1/brightness
  sleep 0.5
  echo 0 > /sys/class/leds/led1/brightness
  sleep 0.5
done
```
- Stop blinking: Ctrl + C

# 4.2 Sequential Blinking (One by One)
```bash
while true; do
  for i in 1 2 3 4; do
    echo 1 > /sys/class/leds/led$i/brightness
    sleep 0.2
    echo 0 > /sys/class/leds/led$i/brightness
  done
done
```
- Stop blinking: Ctrl + C


4.3 Knight Rider Pattern (Back-and-Forth)
```bash
while true; do
  for i in 1 2 3 4; do
    echo 1 > /sys/class/leds/led$i/brightness
    sleep 0.1
    echo 0 > /sys/class/leds/led$i/brightness
  done
  for i in 3 2; do
    echo 1 > /sys/class/leds/led$i/brightness
    sleep 0.1
    echo 0 > /sys/class/leds/led$i/brightness
  done
done
```
- Stop blinking: Ctrl + C


## 🧩 5. Push Button Controlled LED

# Step 1: Export Button GPIO
Assuming SW3 → gpio68:
```bash
echo 68 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio68/direction
```
# Step 2: Button-triggered LED Blink Script
```bash
while true; do
  if [ "$(cat /sys/class/gpio/gpio68/value)" = "0" ]; then
    echo 1 > /sys/class/leds/led1/brightness
    sleep 0.2
    echo 0 > /sys/class/leds/led1/brightness
    sleep 0.2
  else
    echo 0 > /sys/class/leds/led1/brightness
  fi
done
```
- Press SW3: LED1 blinks
- Release SW3: LED1 turns OFF
- Stop script: Ctrl + C

## 🧩 6. Save Scripts for Future Use
```bash
nano /root/button_blink.sh
# Paste the above button-controlled blink script
chmod +x /root/button_blink.sh
./button_blink.sh
```

🧩 7. Summary & Notes

- LEDs can be controlled via /sys/class/leds.
- Multiple blinking patterns are supported: continuous, sequential, Knight Rider.
- Button GPIOs may vary depending on BSP; verify with:

```bash
cat /sys/kernel/debug/gpio
```
- Scripts can be automated at boot using /etc/rc.local or a systemd service.

<div align="center"> <img src="https://img.shields.io/badge/LED_Control_Status-Completed-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/Board-PolarFire®_SoC_Icicle_Kit-red?style=for-the-badge" /> <img src="https://img.shields.io/badge/Platform-EdgeSight_AI_Assistive_Device-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Feature-LED_Control-yellow?style=for-the-badge" /> </div>

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


