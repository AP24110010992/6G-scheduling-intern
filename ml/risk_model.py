import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# Load the dataset
data = pd.read_csv("dataset/UNSW_NB15_training-set.csv")

print("Dataset Loaded Successfully!")
print(data.head())

# Select features and target
X = data[["dur", "proto", "sbytes", "dbytes"]]
y = data["label"]

encoder = LabelEncoder()

X["proto"] = encoder.fit_transform(X["proto"])

# Save the encoder
joblib.dump(encoder, "ml/protocol_encoder.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
# Predict on test data
y_pred = model.predict(X_test)

print("Prediction completed!")

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Save trained model
joblib.dump(model, "ml/random_forest_model.pkl")

print("Model saved successfully!")

# Probability predictions for ROC-AUC
y_prob = model.predict_proba(X_test)[:, 1]
roc = roc_auc_score(y_test, y_prob)

print("\n----- Model Performance -----")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc:.4f}")

# Feature importance
importance = model.feature_importances_

print("\n----- Feature Importance -----")

for feature, score in zip(X.columns, importance):
    print(f"{feature}: {score:.4f}")

    # Save results
with open("results/model_results.txt", "w") as file:
    file.write("Random Forest Results\n")
    file.write("----------------------\n")
    file.write(f"Accuracy : {accuracy:.4f}\n")
    file.write(f"Precision: {precision:.4f}\n")
    file.write(f"Recall   : {recall:.4f}\n")
    file.write(f"F1 Score : {f1:.4f}\n")
    file.write(f"ROC-AUC  : {roc:.4f}\n")

print("\nResults saved to results/model_results.txt")