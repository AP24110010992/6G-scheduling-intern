# Improvement 2: Deep Learning and Explainability

## Objective

The objective of this phase was to investigate deep learning techniques for intrusion detection and to understand which features contribute most to attack prediction.

## Work Completed

- Developed a Multi-Layer Perceptron (MLP) model using TensorFlow.
- Compared MLP performance with the Random Forest model.
- Integrated the MLP model into the IoT security simulation.
- Performed feature importance analysis using the trained Random Forest model.
- Visualized the contribution of individual features to the prediction process.

## Observation

The Random Forest model achieved higher prediction accuracy than the MLP model in the current experiment. Feature importance analysis showed that network traffic attributes such as source bytes and destination bytes had a significant impact on attack detection.

## Future Work

- Improve the MLP using additional network features.
- Generate SHAP explanations in a compatible Python environment.
- Compare multiple deep learning architectures such as CNN and LSTM.