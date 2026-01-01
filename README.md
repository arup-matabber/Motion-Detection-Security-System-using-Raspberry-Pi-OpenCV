# 🔐 Motion Detection Security System using Raspberry Pi & OpenCV

This project implements a **motion detection security system** using a Raspberry Pi, OpenCV, and GPIO-based alerts. It continuously monitors a live video feed, detects motion, triggers LED and buzzer alerts, captures timestamped images, and logs events. The system is cost-effective and suitable for **homes, labs, offices, and IoT surveillance applications**.


## 📌 Introduction

Home and personal security have become essential in modern environments. Automated surveillance systems enable real-time intruder detection and alerting.

This project uses a **Raspberry Pi**, **camera module**, **OpenCV**, and **GPIO components** to detect motion in real time. When motion is detected, the system activates a buzzer and LED, captures an image with a timestamp, and logs the event for future reference.

---

## 🔧 Components Used

### 🖥️ Raspberry Pi 4

* Acts as the main processing unit
* Features: Quad-core CPU, HDMI output, USB ports, and a 40-pin GPIO header

### 📷 USB Camera / Raspberry Pi Camera Module

* Captures real-time video feed for motion detection
* Recommended resolution: **640×480 or higher**

### 💡 LED

* Provides a visual alert when motion is detected
* Forward voltage ≈ **2V**, forward current ≈ **20mA**

### 🔊 Active Buzzer

* Produces an audible alert upon motion detection
* Operates directly using Raspberry Pi GPIO (**3.3V / 5V**)

### 🔌 Breadboard

* Used for prototyping and connecting components without soldering

### 🔗 Jumper Wires (Male-to-Male)

* Connect Raspberry Pi GPIO pins to the LED and buzzer
* Ensure secure and stable electrical connections

### 🧮 Resistor (330Ω – 1kΩ)

* Protects the LED from excessive current

### 🔋 Power Supply (5V / 3A)

* Provides stable and reliable power to the Raspberry Pi

