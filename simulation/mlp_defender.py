# simulation/mlp_defender.py

import joblib
import pandas as pd
from tensorflow.keras.models import load_model

# --------------------------------------------------
# Load trained MLP model and encoder
# --------------------------------------------------

MODEL_PATH = "ml/best_mlp_model.keras"
ENCODER_PATH = "ml/protocol_encoder.pkl"

model = load_model(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

print("✓ MLP Defender loaded successfully")


# --------------------------------------------------
# Predict attack probability
# --------------------------------------------------

def predict_attack_probability(duration, protocol, sbytes, dbytes):
    """
    Returns the probability that the traffic is malicious.

    Parameters
    ----------
    duration : float
    protocol : str
    sbytes : int
    dbytes : int

    Returns
    -------
    float
        Probability between 0 and 1
    """

    protocol_encoded = encoder.transform([protocol])[0]

    sample = pd.DataFrame({
        "dur": [duration],
        "proto": [protocol_encoded],
        "sbytes": [sbytes],
        "dbytes": [dbytes]
    })

    probability = float(
        model.predict(sample, verbose=0)[0][0]
    )

    return probability


# --------------------------------------------------
# Classify traffic
# --------------------------------------------------

def predict_attack(duration, protocol, sbytes, dbytes, threshold=0.5):
    """
    Returns:
        (is_attack, probability)
    """

    probability = predict_attack_probability(
        duration,
        protocol,
        sbytes,
        dbytes
    )

    return probability >= threshold, probability


# --------------------------------------------------
# Example usage
# --------------------------------------------------

if __name__ == "__main__":

    attack, probability = predict_attack(
        duration=2,
        protocol="tcp",
        sbytes=500,
        dbytes=200
    )

    print(f"Attack Probability : {probability:.4f}")

    if attack:
        print("Prediction : Attack Detected")
    else:
        print("Prediction : Normal Traffic")