import joblib
import pandas as pd

# Load trained model
model = joblib.load("ml/random_forest_model.pkl")

# Load protocol encoder
encoder = joblib.load("ml/protocol_encoder.pkl")


def predict_attack(duration, protocol, sbytes, dbytes):

    # Convert protocol using saved encoder
    protocol = encoder.transform([protocol])[0]

    sample = pd.DataFrame({
        "dur": [duration],
        "proto": [protocol],
        "sbytes": [sbytes],
        "dbytes": [dbytes]
    })

    prediction = model.predict(sample)[0]

    if prediction == 1:
        print("Attack Detected")
    else:
        print("Normal Traffic")


# Example
predict_attack(2, "tcp", 500, 200)