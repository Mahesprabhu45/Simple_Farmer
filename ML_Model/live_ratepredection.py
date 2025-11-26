import requests
import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression
import json

# 🔧 CONFIG
LAT, LON = 11.9964132, 76.7419713
STATE = "Karnataka"
DISTRICT = "Chamrajnagar"
COMMODITY = "Tomato"
API_KEY = "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"
RESOURCE_ID = "35985678-0d79-46b4-9ed6-6f13308a1d24"
FIREBASE_URL = "https://upkisaan-6246b-default-rtdb.firebaseio.com/homepage_alert/Message 2.json"

# 🗓 Date range
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=730)  # 2 years

# 📦 Fetch weather data
weather_url = (
    f"https://archive-api.open-meteo.com/v1/era5?"
    f"latitude={LAT}&longitude={LON}&start_date={start_date}&end_date={end_date}"
    f"&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&timezone=Asia%2FKolkata"
)

weather_res = requests.get(weather_url)
weather = weather_res.json()["daily"]

# 🎯 Filter every 3rd day
filtered = []
for i, date in enumerate(weather["time"]):
    if int(date[-2:]) % 3 == 0:
        filtered.append({
            "date": date,
            "max": weather["temperature_2m_max"][i],
            "min": weather["temperature_2m_min"][i],
            "avg": weather["temperature_2m_mean"][i]
        })

# 💰 Fetch tomato prices
def get_price(date):
    url = (
        f"https://api.data.gov.in/resource/{RESOURCE_ID}?api-key={API_KEY}&format=json&limit=1"
        f"&filters[State.keyword]={STATE}&filters[District.keyword]={DISTRICT}"
        f"&filters[Commodity.keyword]={COMMODITY}&filters[Arrival_Date]={date}"
    )
    try:
        res = requests.get(url).json()
        if res["records"]:
            return float(res["records"][0]["Modal_Price"])
    except Exception as e:
        print(f"⚠ Error fetching price for {date}: {e}")
    return None

# 📋 Combine data
records = []
for entry in filtered:
    price = get_price(entry["date"])
    if price:
        records.append({
            "date": entry["date"],
            "avg_temp": entry["avg"],
            "price": price
        })

df = pd.DataFrame(records)

# 📈 Predict tomato price using linear regression
if len(df) >= 2:
    X = df[["avg_temp"]]
    y = df["price"]
    model = LinearRegression().fit(X, y)
    last_temp = [[df.iloc[-1]["avg_temp"]]]
    predicted_price = int(round(model.predict(last_temp)[0]))
    print(f"📊 Predicted Price: ₹{predicted_price}")

    # 🔥 Push to Firebase
    firebase_res = requests.put(FIREBASE_URL, data=json.dumps(predicted_price))
    print("✅ Firebase Response:", firebase_res.text)
else:
    print("❌ Not enough data to predict.")