
<div align="center">

  <h1>💡 Web-Based LED Control — PolarFire® SoC Icicle Kit</h1>
  
  <p>
	This directory demonstrates how to control the on-board LEDs of the 
	<b>PolarFire® SoC Icicle Kit</b> using a simple 
	<b>web-based interface</b> built with Python Flask.  
	Users can toggle each LED (ON/OFF) directly from any browser connected over the local Ethernet network.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
	<img src="../Tool Installation & Setup Guide/Images/mic.png" width="200" alt="Microchip Technology logo">
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Interface-Web_Control-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python_&_HTML-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-orange?style=for-the-badge" />

</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Overview** | [Jump to Section](#1-overview) |
| 2 | **Board LED Interface** | [Jump to Section](#2-board-led-interface) |
| 3 | **Project Folder Structure** | [Jump to Section](#3-project-folder-structure) |
| 4 | **Flask Server Code** | [Jump to Section](#4-flask-server-code) |
| 5 | **HTML Web Interface** | [Jump to Section](#5-html-web-interface) |
| 6 | **How to Run** | [Jump to Section](#6-how-to-run) |
| 7 | **Demonstration** | [Jump to Section](#7-demonstration) |
| 8 | **Additional Notes** | [Jump to Section](#8-additional-notes) |

---

## 1. Overview

This guide explains how to build and run a **web-based LED control panel** on the Icicle Kit.  
The Flask server exposes endpoints that directly manipulate the **Linux LED sysfs interface**, allowing control over the on-board LEDs through a browser.

Key features:
- No extra Python libraries required  
- Runs locally on the Icicle Kit (Linux)  
- Controls 4 on-board LEDs via web buttons  
- Real-time LED control from any device in the network  

---

## 2. Board LED Interface

On the PolarFire® SoC Linux environment, each LED is exposed as a file under:

```
/sys/class/leds/led1/brightness
/sys/class/leds/led2/brightness
/sys/class/leds/led3/brightness
/sys/class/leds/led4/brightness
```

Commands:
```bash
# Turn ON LED1
echo 1 > /sys/class/leds/led1/brightness

# Turn OFF LED1
echo 0 > /sys/class/leds/led1/brightness
```

---

## 3. Project Folder Structure

mpfs_led_web/
│
├── led_web.py              # Python Flask server
├── README.md               # Documentation
│
└── templates/
	└── index.html          # HTML interface for LED control

---

## 4. Flask Server Code

Below is the complete Python code for the web server:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Map LEDs to sysfs brightness paths
led_paths = {
	"led1": "/sys/class/leds/led1/brightness",
	"led2": "/sys/class/leds/led2/brightness",
	"led3": "/sys/class/leds/led3/brightness",
	"led4": "/sys/class/leds/led4/brightness"
}

# Function to write LED value
def set_led(led, value):
	if led in led_paths:
		try:
			with open(led_paths[led], "w") as f:
				f.write(str(value))
		except PermissionError:
			# Running on-board requires root or proper permissions
			return False
		except Exception:
			return False
		return True
	return False

# Flask routes
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/on/<led>")
def led_on(led):
	set_led(led, 1)
	return f"{led} ON"

@app.route("/off/<led>")
def led_off(led):
	set_led(led, 0)
	return f"{led} OFF"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
```

---

## 5. HTML Web Interface

Create `templates/index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>MPFS LED Control</title>
	<script>
		function sendCommand(led, action) {
			fetch(`/${action}/${led}`)
				.then(res => res.text())
				.then(console.log);
		}
	</script>
	<style>
		body { font-family: Arial, sans-serif; padding: 20px; }
		.led-card { border: 1px solid #ddd; padding: 12px; margin: 8px 0; border-radius: 6px; }
		button { margin-right: 8px; padding: 8px 12px; }
	</style>
</head>
<body>
	<h1>MPFS LED Control</h1>

	<div class="led-card">
		<h2>LED 1</h2>
		<button onclick="sendCommand('led1', 'on')">ON</button>
		<button onclick="sendCommand('led1', 'off')">OFF</button>
	</div>

	<div class="led-card">
		<h2>LED 2</h2>
		<button onclick="sendCommand('led2', 'on')">ON</button>
		<button onclick="sendCommand('led2', 'off')">OFF</button>
	</div>

	<div class="led-card">
		<h2>LED 3</h2>
		<button onclick="sendCommand('led3', 'on')">ON</button>
		<button onclick="sendCommand('led3', 'off')">OFF</button>
	</div>

	<div class="led-card">
		<h2>LED 4</h2>
		<button onclick="sendCommand('led4', 'on')">ON</button>
		<button onclick="sendCommand('led4', 'off')">OFF</button>
	</div>
</body>
</html>
```

---

## 6. How to Run

1️⃣ Ensure Folder Structure

```
mpfs_led_web/
├── led_web.py
└── templates/
	└── index.html
```

2️⃣ Run the Flask Server

```powershell
python led_web.py
```

3️⃣ Access the Web Interface
Open a browser on your laptop and go to:

```
http://<board-ip>:5000/
```

For example:

```
http://192.168.137.25:5000/
```

4️⃣ Control LEDs
Click ON/OFF buttons for each LED to toggle the respective on-board light.

---

## 7. Demonstration

<div align="center">
  <img src="Images/webled-1.jpg" width="750" alt="Web Interface for LED Control">
  <p><i>Figure 1: Browser-based LED control panel hosted on the Icicle Kit</i></p>
</div>

<div align="center">
  <img src="Images/webled-2.jpg" width="750" alt="LEDs on PolarFire® SoC Icicle Kit lighting up">
  <p><i>Figure 2: On-board LEDs responding to web commands in real-time</i></p>
</div>

---

## 8. Additional Notes

- No external GPIO libraries or dependencies required.
- Uses the Linux sysfs interface for direct LED control.
- Can be extended to include blinking patterns or status indicators.
- Works seamlessly with your Ethernet Internet Connection setup.

---

<div align="center">

© 2025 VLSI Design Contest – EdgeSight Project Team
Powered by Microchip PolarFire® SoC Technology

</div>

---

### Save & Image placement

Place the two images in this folder:

```
Web-based_led_control/Images/webled-1.jpg
Web-based_led_control/Images/webled-2.jpg
```

Notes:
- The file above is now your single `README.md` for the web LED control demo.
- If you want, I can also create the `led_web.py` and `templates/index.html` files in this repo and add a small commit instruction to push them to your GitHub — tell me if you want me to do that.
