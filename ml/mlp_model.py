import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import AUC

data = pd.read_csv("dataset/UNSW_NB15_training-set.csv")
print("Dataset Loaded")

X = data[["dur", "proto", "sbytes", "dbytes"]]
y = data["label"]

encoder = LabelEncoder()

X["proto"] = encoder.fit_transform(X["proto"])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = Sequential([
    Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    Dense(32, activation="relu"),
    Dense(16, activation="relu"),
    Dense(1, activation="sigmoid")
])
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy", AUC(name="auc")]
)
history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)
loss, accuracy, auc = model.evaluate(X_test, y_test)

print("\nModel Evaluation")
print("----------------")
print(f"Accuracy : {accuracy:.4f}")
print(f"AUC      : {auc:.4f}")

model.save("ml/best_mlp_model.keras")
print("\nMLP model saved successfully!")
