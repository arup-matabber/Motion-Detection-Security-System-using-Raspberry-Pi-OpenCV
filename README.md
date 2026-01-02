# 🛡️ Motion Detection Security System using Raspberry Pi & OpenCV

A **real-time motion detection security system** built using **Raspberry Pi**, **OpenCV**, and **GPIO-based alerts**.
The system continuously monitors live camera feed, detects motion, triggers **LED & buzzer alerts**, captures snapshots with timestamps, and logs intrusion events.

---

## 📌 Project Overview

In modern environments, **automated surveillance systems** are essential for ensuring safety and security.
This project implements a **cost-effective IoT-based motion detection system** suitable for:

* 🏠 Home Security
* 🧪 Laboratories
* 🏢 Offices
* 🌐 IoT Surveillance Applications

### Key Highlights

* Real-time motion detection
* Visual & audible alerts
* Snapshot capture with timestamp
* Event logging
* Continuous live monitoring

---

## 🧠 System Architecture

### Block Diagram (Logical Flow)

```
USB / Pi Camera
      ↓
Raspberry Pi (OpenCV Processing)
      ↓
Motion Detection Algorithm
      ↓
GPIO Control
 ├── LED Alert
 └── Buzzer Alert
      ↓
Snapshot + Event Logging
```

---

## 🔧 Hardware Components Used

| Component                  | Description                            |
| -------------------------- | -------------------------------------- |
| **Raspberry Pi 4**         | Main processing unit with GPIO support |
| **USB Camera / Pi Camera** | Captures real-time video feed          |
| **LED**                    | Visual alert on motion detection       |
| **Active Buzzer**          | Audible alert                          |
| **Breadboard**             | Prototyping                            |
| **Jumper Wires**           | GPIO connections                       |
| **Resistor (330Ω–1kΩ)**    | LED current protection                 |
| **5V / 3A Power Supply**   | Stable power for Raspberry Pi          |

---

## 🔌 GPIO Pin Configuration

| Component | GPIO Pin | Physical Pin |
| --------- | -------- | ------------ |
| LED       | GPIO 18  | Pin 12       |
| Buzzer    | GPIO 23  | Pin 16       |
| Ground    | GND      | Pin 6        |

---

## 🛠️ Software Requirements

* **Python 3**
* **OpenCV**
* **NumPy**
* **RPi.GPIO**
* **Raspberry Pi OS**

### Install Dependencies

```bash
sudo apt update
sudo apt install python3-opencv
pip3 install numpy RPi.GPIO
```

---

## 📂 Project Structure

```
motion-detection-security-system/
│
├── motion_detection.py
├── motion_log.txt
├── motion_YYYYMMDD_HHMMSS.jpg
├── README.md
```


## ▶️ How to Run

```bash
python3 motion_detection.py
```

* Press **`Q`** to exit safely
* Ensure camera is connected before running

---

## 📊 Results & Observations

* ✅ Accurate real-time motion detection
* 🚨 LED & buzzer trigger instantly
* 🖼️ Snapshots saved with timestamps
* 📝 Log file records all motion events
* 🔄 Automatically resets after motion stops

---

## 🎯 Conclusion

This project successfully demonstrates a **low-cost, real-time motion-based security system** using open-source tools.

### Achievements

✔ Real-time surveillance
✔ Automated alerts
✔ Event logging
✔ Continuous monitoring

### Future Enhancements

* ☁️ Cloud storage integration
* 📱 Mobile notifications
* 🤖 AI-based person/object detection
* 🔔 Email / SMS alerts

---

## 📽️ Demo Video

🎥 **Project Demo:**
[https://drive.google.com/file/d/1h7qn4-MFaGpqeZl8NiiY77qRt_y_N0_Z/view](https://drive.google.com/file/d/1h7qn4-MFaGpqeZl8NiiY77qRt_y_N0_Z/view)

---

## 📚 References

* OpenCV Documentation — [https://opencv.org](https://opencv.org)
* Raspberry Pi Docs — [https://www.raspberrypi.com/documentation/](https://www.raspberrypi.com/documentation/)
* Python GPIO Documentation
