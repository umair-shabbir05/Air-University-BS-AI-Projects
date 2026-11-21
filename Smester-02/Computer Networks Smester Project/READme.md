# 🌐 AI-Based Network Monitoring System – Computer Networks Semester Project

## 📌 Project Overview

This project is an **AI-Based Network Monitoring System** developed as a semester project for the subject **Computer Networks**.

The system uses an ESP32 microcontroller with built-in Wi-Fi capabilities to monitor the connectivity status of selected devices connected to a Wi-Fi network.

It provides real-time status information through an OLED display, while LEDs and a buzzer provide visual and audio notifications when a monitored device becomes offline.

The project demonstrates the practical application of computer networking, IoT, and embedded systems.

## 🎯 Project Objectives

- Monitor the connectivity status of devices connected to a Wi-Fi network.
- Identify whether selected devices are online or offline.
- Display device status using an OLED display.
- Provide visual notifications using LEDs.
- Generate sound alerts through a buzzer when a device disconnects.
- Develop a low-cost network monitoring solution.

## 🛠️ Technologies and Components Used

### Hardware Components

- ESP32 Microcontroller
- OLED Display
- Green LEDs
- Red LEDs
- Buzzer
- Breadboard
- Jumper Wires
- Resistors
- Wi-Fi Router
- USB Power Supply

### Software and Libraries

- **Arduino IDE:** Development environment.
- **C/C++:** Programming language.
- **WiFi.h:** Wi-Fi communication.
- **Adafruit SSD1306:** OLED display control.

## ⚙️ Working Principle

The ESP32 connects to a Wi-Fi router and monitors selected devices on the network.

The system checks whether the monitored devices are reachable and updates their connectivity status.

The system uses the following indicators:

| Device Status | Green LED | Red LED | Buzzer |
|---|---|---|---|
| Online | ON | OFF | OFF |
| Offline | OFF | ON | Sound Alert |

The OLED display continuously shows the current online and offline status of the monitored devices.

The current implementation is configured to monitor three devices.

## ✨ System Features

- Real-time connectivity monitoring.
- Monitoring of up to three selected devices.
- Online and offline device detection.
- OLED-based status display.
- Green and red LED indicators.
- Audio notifications using a buzzer.
- ESP32-based wireless connectivity.

## 🔌 Hardware Description

### ESP32 Microcontroller
Acts as the main controller, handling Wi-Fi communication and controlling the connected hardware components.

### OLED Display
Displays the current connectivity status of monitored devices.

### Green and Red LEDs
Green LEDs indicate online devices, while red LEDs indicate offline devices.

### Buzzer
Generates an audio alert whenever a monitored device becomes disconnected.

### Wi-Fi Router
Provides the wireless network through which the ESP32 and monitored devices communicate.

## 📂 Project Structure

```text
Computer-Networks-Project/
│
├── AI_Based_Network_Monitoring_System_Report.pdf
├── README.md
│
└── Project-Resources/
    ├── Circuit-Diagram/
    └── Hardware-Screenshots/
```

## ▶️ How to Run the Project

1. Download the project repository.
2. Install Arduino IDE.
3. Connect the ESP32 to your computer.
4. Install the required OLED display library.
5. Configure the Wi-Fi credentials in the source code.
6. Connect the LEDs, buzzer, and OLED display according to the circuit design.
7. Upload the program to the ESP32.
8. Connect the ESP32 to the Wi-Fi network and observe the device monitoring output.

**Requirements:** ESP32 board, Arduino IDE, required libraries, Wi-Fi router, and the hardware components listed above.

## 📚 Concepts Learned

Through this project, I gained practical experience in:

- Wi-Fi communication and networking.
- Network device connectivity monitoring.
- ESP32 microcontroller programming.
- IoT-based system development.
- Interfacing electronic components.
- OLED display communication using I2C.
- Visual and audio notification systems.

## ⚠️ Current Limitations

- The current implementation monitors three devices.
- The system depends on Wi-Fi availability.
- Advanced network traffic analysis is not implemented.
- Mobile application and cloud monitoring are not included.

## 🚀 Future Improvements

- Integrate cloud-based network monitoring.
- Develop a mobile application for remote monitoring.
- Add support for more network devices.
- Introduce advanced network traffic analysis.
- Implement intelligent anomaly detection.
- Add email or SMS notifications.

## 🎓 Academic Information

- **Student:** Umair Shabbir
- **Registration ID:** 2502027
- **University:** Air University Islamabad (Main Campus)
- **Degree:** BS Artificial Intelligence
- **Semester:** 2nd Semester
- **Subject:** Computer Networks
- **Project:** AI-Based Network Monitoring System

---

*Developed as an academic project to explore the practical applications of computer networking, IoT, and embedded systems.*
