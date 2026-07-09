import joblib
import matplotlib.pyplot as plt

# Load the trained Random Forest model
model = joblib.load("ml/random_forest_model.pkl")

# Feature names used during training
feature_names = ["dur", "proto", "sbytes", "dbytes"]

# Get feature importance scores
importance = model.feature_importances_

# Print feature importance
print("Feature Importance")
print("-" * 30)

for name, score in zip(feature_names, importance):
    print(f"{name:10} : {score:.4f}")

# Plot
plt.figure(figsize=(7, 5))

plt.bar(feature_names, importance)

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")

plt.tight_layout()

plt.savefig("results/feature_importance.png", dpi=150)

plt.show()

print("\nGraph saved as results/feature_importance.png")