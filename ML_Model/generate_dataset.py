import pandas as pd
import random

rows = 300
data = []

for _ in range(rows):
    humidity = random.randint(45,95)
    motion = random.randint(0,1)
    npk = random.randint(80,160)
    rain = random.choice(["Yes","No"])
    sm30 = random.randint(30,100)
    sm60 = sm30 + random.randint(-5,15)
    temp = random.randint(18,38)
    wind = random.randint(2,20)

    if humidity > 80 and sm30 > 70:
        label = "Blight"
    elif temp > 34 and sm30 < 50:
        label = "Rust"
    elif npk > 140 and humidity > 70:
        label = "Wilt"
    else:
        label = "Healthy"

    data.append([humidity, motion, npk, rain, sm30, sm60, temp, wind, label])

df = pd.DataFrame(data, columns=[
    "humidity","motionDetected","npkValue","rainStatus",
    "soilMoisture30","soilMoisture60","temperature","windSpeed","Disease Label"
])

df.to_csv("SmartFarm_Dataset.csv", index=False)
print("Dataset created successfully: SmartFarm_Dataset.csv")
