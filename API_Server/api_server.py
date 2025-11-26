from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("../ML_Model/model.pkl", "rb"))
encoder = pickle.load(open("../ML_Model/encoder.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    df = pd.DataFrame([data])
    df['rainStatus'] = encoder.transform(df['rainStatus'])

    prediction = model.predict(df)[0]

    return jsonify({
        "prediction": prediction,
        "status": "success"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
