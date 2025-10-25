<div align="center">

  <h1>🌐 Ethernet Internet Connection — PolarFire® SoC Icicle Kit</h1>
  
  <p>
    This directory documents the step-by-step process of enabling 
    <b>Internet connectivity via Ethernet</b> for the 
    <b>PolarFire® SoC Icicle Kit</b> using a Windows laptop as the internet source.
    It allows the board to access the network for package updates, remote repositories, 
    and communication with cloud or local servers.
  </p>

  <a href="https://www.microchip.com/" target="_blank">
    <img src="../Tool Installation & Setup Guide/Images/mic.png" width="200" alt="Microchip Technology logo">
  </a>

  <br><br>
  <img src="https://img.shields.io/badge/Interface-Ethernet-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-PolarFire®_SoC-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Internet_Connectivity-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-orange?style=for-the-badge" />

</div>

---

# 📘 Table of Contents

| 🔢 # | 📂 Topic | 🔗 Link |
|------|----------|---------|
| 1 | **Overview** | [Jump to Section](#1-overview) |
| 2 | **Windows Laptop Configuration** | [Jump to Section](#2-windows-laptop-configuration) |
| 3 | **Icicle Kit Network Setup** | [Jump to Section](#3-icicle-kit-network-setup) |
| 4 | **Testing Internet Connection** | [Jump to Section](#4-testing-internet-connection) |
| 5 | **Troubleshooting** | [Jump to Section](#5-troubleshooting) |
| 6 | **Summary** | [Jump to Section](#6-summary) |

---

## 1. Overview

This section provides the procedure to enable **Internet connectivity** on the **PolarFire® SoC Icicle Kit** through an **Ethernet cable connection** shared from a **Windows laptop**.

By following this setup, the Icicle Kit will be able to:
- Access online repositories (e.g., `apt`, `git`)
- Communicate with external servers
- Perform software and package updates
- Host web-based applications (Flask, Django, etc.)

---

## 2. Windows Laptop Configuration

Perform the following steps on your **Windows laptop** to enable **Internet Connection Sharing (ICS)**.

1️⃣ **Connect Laptop to Internet**  
   - Connect via **Wi-Fi** or **LAN** (ensure internet access is active).

2️⃣ **Connect Ethernet Cable**  
   - Use an **Ethernet cable** to connect your laptop to the **MPFS Icicle Kit** board.

3️⃣ **Enable Internet Connection Sharing (ICS)**  
   - Open **Control Panel → Network and Internet → Network Connections**  
   - Right-click your active Internet adapter (e.g., Wi-Fi) → **Properties**  
   - Go to the **Sharing** tab  
   - Check ✅ *“Allow other network users to connect through this computer’s Internet connection”*  
   - Under *“Home networking connection”*, select **Ethernet**  

> 💡 Windows automatically assigns **192.168.137.1** to the Ethernet adapter.

---

## 3. Icicle Kit Network Setup

After connecting and powering the board, open a **serial terminal** (e.g., PuTTY at 115200 baud) and run the following commands:

### Step 1: Bring up the Ethernet interface
```bash
ip link set eth0 up
```

### Step 2: Verify IP address
ip addr show eth0


Expected output includes:
```bash
inet 192.168.137.xx/24
```

If not assigned automatically, you can manually set it:
```bash
ip addr add 192.168.137.25/24 dev eth0
```
### Step 3: Configure default gateway
```bash
ip route add default via 192.168.137.1 dev eth0
```
### Step 4: Add DNS servers
```bash
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
```
## 4. Testing Internet Connection

Verify connectivity using ping:
```bash
ping -c 4 8.8.8.8      # Test network reachability
ping -c 4 google.com   # Test DNS resolution
```

Successful pings indicate that the Icicle Kit is connected to the internet via the laptop.
