🌾 Smart Farm Automation Using IoT + Machine Learning

This project combines ESP32 IoT hardware, real-time sensors, and a machine learning model to automate farming decisions such as irrigation, disease prediction, and environment monitoring.
A mobile app acts as a dashboard allowing remote control and real-time insights.

📌 Features

Crop Disease Prediction using ML

Automated Irrigation based on Soil Moisture + Rain Status

PIR-based Intrusion Alerts (Animals/Birds)

ESP32 Live Sensor Data Streaming

Mobile App (MIT App Inventor) Control Panel

Integration with Weather, AQI, Soil, and Market APIs

ML accuracy ~80–90% depending on dataset and conditions

🧠 Machine Learning Model

Attribute	Details
Algorithm	Logistic Regression
Dataset	Real + Synthetic sensor dataset
Training Files	generate_dataset.py, train_model.py
Output	model.pkl, encoder.pkl, accuracy report
Run the model:
python generate_dataset.py
python train_model.py

🛰 Real-Time Data Sources Used

Purpose	    Source
Soil Moisture Satellite Data	ISRO
Real-Time AQI	data.gov.in
Soil Moisture API	data.gov.in
Market Commodity Prices	Mandi.gov
Weather Forecasting	OpenWeather API

🛠 Hardware Setup

Component	Use
ESP32	    Main controller
Soil Moisture Sensor	    Irrigation logic
Rain Sensor	             Avoid watering during rain
DHT22/BME280	Temperature + humidity
PIR Sensor	Animal detection
Relay Module	Water pump switching
Water Pump	Irrigation

🧩 Complete circuit and wiring diagrams are in:

/Hardware/
├── Component_List.pdf
├── Wiring_Diagram.png
└── Circuit_Schematic.fzz

📂 Project Folder Structure
Smart_Farm_IoT_ML/
│
├── ML_Model/
│   ├── generate_dataset.py
│   ├── train_model.py
│   ├── SmartFarm_Dataset.csv
│   ├── model.pkl
│   └── encoder.pkl
│
├── ESP32_Firmware/
│   └── smart_farm_controller.ino
│
├── API_Server/
│   ├── api_server.py
│   ├── model.pkl
│   └── encoder.pkl
│
├── Mobile_App/
│   ├── SmartFarmApp.aia
│   └── App_Images/
│
├── Hardware/
│   ├── Component_List.pdf
│   ├── Wiring_Diagram.png
│   └── Circuit_Schematic.fzz
│
├── screenshots/
├── requirements.txt
└── README.md

📱 Mobile App (MIT App Inventor)

Live dashboard

Pump ON/OFF control

Disease prediction request

Sensor status panel

APK and AIA available in /Mobile_App/.

🧩 API Server

Runs on Flask and connects ML model with ESP32 and the mobile app.

Start server:

python api_server.py


Endpoint:

POST  /predict

🚀 Future Improvements

TensorFlow Lite on ESP32 (Edge AI)

LoRaWAN farm-scale deployment

Fertilizer recommendation using NPK sensor

Multi-crop disease model


🔗 LinkedIn: www.linkedin.com/in/mahesh-prabhu-6063b929a
