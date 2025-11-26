import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

print("🔄 Loading dataset...")

# Load dataset
data = pd.read_csv("SmartFarm_Dataset.csv")
print("✅ Dataset loaded successfully!")

# Separate features and labels
X = data[['humidity', 'motionDetected', 'npkValue', 'rainStatus',
          'soilMoisture30', 'soilMoisture60', 'temperature', 'windSpeed']]
y = data['Disease Label']

# Encode categorical column
encoder = LabelEncoder()
X['rainStatus'] = encoder.fit_transform(X['rainStatus'])

# Split data
print("📊 Splitting training and testing data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("🤖 Training Logistic Regression model...")
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
accuracy = accuracy_score(y_test, y_pred)

print("\n🎉 TRAINING COMPLETE 🎉\n")
print(f"📌 Model Accuracy: {round(accuracy * 100, 2)}%\n")
print("📌 Classification Report:\n")
print(classification_report(y_test, y_pred))
print("📌 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Test new sample
new_data = pd.DataFrame({
    'humidity': [70],
    'motionDetected': [0],
    'npkValue': [130],
    'rainStatus': ['Yes'],
    'soilMoisture30': [65],
    'soilMoisture60': [75],
    'temperature': [29],
    'windSpeed': [7]
})

new_data['rainStatus'] = encoder.transform(new_data['rainStatus'])

prediction = model.predict(new_data)[0]
print(f"\n🌱 Predicted Disease for New Sample: {prediction}")

print("\n✔ Script executed successfully.\n")
