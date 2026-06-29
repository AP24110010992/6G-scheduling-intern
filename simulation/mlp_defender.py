import joblib
import pandas as pd
from tensorflow.keras.models import load_model

# Load trained MLP model
model = load_model("ml/best_mlp_model.keras")

# Load protocol encoder
encoder = joblib.load("ml/protocol_encoder.pkl")

print("MLP model loaded successfully!")

import joblib
import pandas as pd
from tensorflow.keras.models import load_model

# Load model
model = load_model("ml/best_mlp_model.keras")

# Load encoder
encoder = joblib.load("ml/protocol_encoder.pkl")


def predict_attack(duration, protocol, sbytes, dbytes):

    protocol = encoder.transform([protocol])[0]

    sample = pd.DataFrame({
        "dur": [duration],
        "proto": [protocol],
        "sbytes": [sbytes],
        "dbytes": [dbytes]
    })

    prediction = model.predict(sample, verbose=0)

    if prediction[0][0] > 0.5:
        print("Attack Detected")
    else:
        print("Normal Traffic")


predict_attack(2, "tcp", 500, 200)