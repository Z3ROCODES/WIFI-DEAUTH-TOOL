# WiFi Security Tester 🔒⚡️

[![GitHub](https://img.shields.io/github/license/Z3ROCODES/WIFI-DEAUTH-TOOL)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)  
[![Status](https://img.shields.io/badge/status-educational%20use%20only-yellow)](https://opensource.org/licenses/MIT)

---

## 🚨 Disclaimer

**This tool is for educational and security testing purposes only.**  
Use it only on networks you own or have explicit permission to test. Unauthorized use is **illegal** and may violate cybercrime laws in many countries.

---

## 📜 About

The **WiFi Security Tester** is a Python tool that simulates a **WiFi Deauthentication Attack**, commonly used in penetration testing to test the **security** and **resilience** of a wireless network. It sends **deauthentication packets** to disconnect devices from a WiFi network.

- **What it does**: Simulates deauthentication attacks to test if a network can withstand them.
- **Ideal for**: Ethical hackers, penetration testers, and WiFi security enthusiasts.

---

## ⚙️ Features

- **Disconnect specific devices** from the network.
- **Send deauth packets** to a targeted device or all devices on the network.
- **Customizable attack**: Select the monitor mode interface, target MAC, and access point MAC.

---

## 🛠️ Requirements

- **Linux OS** (Kali Linux, Ubuntu, etc.)
- **Python 3.x** (Install from [python.org](https://www.python.org/))
- **Scapy library** (`pip install scapy`)
- **Monitor mode enabled** on a WiFi adapter
- **Aircrack-ng tools** (`sudo apt install aircrack-ng`)

---

## 🔧 Installation

1. **Install dependencies**:
    ```bash
    sudo apt update
    sudo apt install aircrack-ng
    pip install scapy
    ```

2. **Enable monitor mode on your WiFi adapter**:
    ```bash
    sudo airmon-ng start wlan0
    ```

---

## 🚀 Usage

1. **Run the script**:
    ```bash
    sudo python3 deauth.py
    ```

2. **Input the following**:
    - **Monitor Mode Interface** (e.g., `wlan0mon`)
    - **AP MAC Address** (router’s MAC)
    - **Target MAC** (`FF:FF:FF:FF:FF:FF` for all devices)

3. **The attack will continuously send deauth packets** to disconnect the target device(s).

---

## ⚠️ Legal Warning

**Only use this tool for testing networks you own or have explicit permission to test.**  
Unauthorized use of this tool on external networks is **illegal** and may result in criminal charges. Always respect privacy and security.

---

## 📜 License

This project is released under the **MIT License**. See `LICENSE` for more details.

---

## 👨‍💻 Contributing

Feel free to fork and contribute! For bugs, feature requests, or improvements, open an issue or submit a pull request. Please ensure all contributions align with the project's goal: **educational use only.**

---

## 📝 Acknowledgments

- **Scapy** for providing the packet crafting framework.
- **Aircrack-ng** for making WiFi testing tools available.
- **Python community** for making Python a great language for security research!

---

**Created by [Z3RO](https://github.com/Z3ROCODES)**