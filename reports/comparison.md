# Comparison of Rule-Based Detection and Random Forest Model

## Overview

In Week 2, a rule-based detection approach was implemented to identify attacks in the IoT network. The defender monitored selected nodes and detected attacks based on increases in risk score.

In Week 3, a Random Forest machine learning model was trained using the UNSW-NB15 dataset to classify network traffic as either normal or malicious.

## Comparison

| Feature | Rule-Based Detection | Random Forest Model |
|---------|----------------------|---------------------|
| Detection Method | Fixed rules | Machine Learning |
| Uses Training Data | No | Yes |
| Learns from Previous Data | No | Yes |
| Decision Making | Risk threshold | Pattern recognition |
| Adaptability | Low | High |
| Accuracy | Depends on rules | 93.17% |
| Scalability | Limited | Suitable for large datasets |

## Conclusion

The Random Forest model provides better attack detection because it learns patterns from historical network traffic instead of relying on predefined rules. This makes it more suitable for identifying different types of cyber attacks in IoT networks.