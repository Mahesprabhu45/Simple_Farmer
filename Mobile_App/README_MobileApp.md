📱 Smart Farm Mobile Application

This app is built using MIT App Inventor to remotely monitor and control the Smart Farm IoT System.

🔧 Features:

🌡 View Temperature & Humidity

💧 Soil Moisture Monitoring

🚿 Turn ON/OFF Irrigation Pump

👨‍🌾 Disease Prediction Button (sends request to API server)

☔ Rain detection alert

🐾 Animal intrusion alert from PIR sensor

📊 Real-time UI dashboard

📲 How to Use:

Install SmartFarmApp.apk on your mobile (Android only)

Ensure ESP32 and phone are on the same Wi-Fi network

Open app → enter server IP address

Click "Connect"

Dashboard updates in real-time

🛠 Requirements:
Feature	Technology
Communication	HTTP POST / MQTT
Platform	MIT App Inventor
OS	Android
🔥 Screenshots

(put screenshots here inside the folder)

🧩 App Logic Summary
User Action --> HTTP Request --> Flask API --> ML Model --> Response --> UI update

📌 Future Improvements

Firebase cloud sync

Voice assistant control

Offline mode with local ML