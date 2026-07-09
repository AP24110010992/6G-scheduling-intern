import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

# Load trained Random Forest model
model = joblib.load("ml/random_forest_model.pkl")

# Load dataset
data = pd.read_csv("dataset/UNSW_NB15_training-set.csv")

# Select the same features used for training
X = data[["dur", "proto", "sbytes", "dbytes"]]

# Encode protocol
encoder = joblib.load("ml/protocol_encoder.pkl")
X["proto"] = encoder.transform(X["proto"])

# Create SHAP explainer
explainer = shap.TreeExplainer(model)

# Compute SHAP values
shap_values = explainer.shap_values(X)

# Summary plot
shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.savefig("results/shap_summary.png", dpi=150)
plt.close()

print("SHAP summary saved!")