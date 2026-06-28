# Improvement 1: Machine Learning-Based Attack Detection

## Objective

The objective of this improvement was to replace the rule-based attack detection system with a machine learning approach using a Random Forest classifier.

## Work Completed

- Explored the UNSW-NB15 dataset.
- Selected important network traffic features.
- Trained a Random Forest classifier.
- Achieved an accuracy of 93.17%.
- Saved the trained model and protocol encoder.
- Integrated the trained model into the IoT security simulation.
- Created an ML-based defender for attack prediction.

## Benefits

Compared to the rule-based system, the Random Forest model can learn patterns from historical data and classify network traffic more accurately. This improves attack detection and makes the system more adaptable to different types of cyber attacks.

## Future Improvements

- Train using additional network features.
- Compare multiple machine learning algorithms.
- Integrate real-time attack detection into the simulation.
- Improve model performance using feature engineering and hyperparameter tuning.