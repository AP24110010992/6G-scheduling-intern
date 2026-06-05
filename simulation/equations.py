import math

# -----------------------------
# 1. Defender Utility Function
# Ud = αD − βC
# -----------------------------

def defender_utility(alpha, detected_attacks, beta, compromised_devices):
    return (alpha * detected_attacks) - (beta * compromised_devices)


# -----------------------------
# 2. Attacker Utility Function
# Ua = γC − δD
# -----------------------------

def attacker_utility(gamma, compromised_devices, delta, detected_attacks):
    return (gamma * compromised_devices) - (delta * detected_attacks)


# -----------------------------
# 3. ML Risk Prediction
# RiML = f(xi)
# -----------------------------

def ml_risk_prediction(vulnerability, past_behavior):
    return (0.6 * vulnerability) + (0.4 * past_behavior)


# -----------------------------
# 4. Risk Score Update
# Ri = λRi + (1 − λ)RiML
# -----------------------------

def update_risk(current_risk, ml_risk, lamda):
    return (lamda * current_risk) + ((1 - lamda) * ml_risk)


# -----------------------------
# 5. Detection Probability
# -----------------------------

def detection_probability(theta1, risk_score, theta2, monitoring_factor):
    exponent = -(theta1 * risk_score - theta2 * monitoring_factor)
    return 1 / (1 + math.exp(exponent))


# -----------------------------
# Sample Testing
# -----------------------------

print("Defender Utility:",
      defender_utility(2, 10, 1, 3))

print("Attacker Utility:",
      attacker_utility(3, 5, 1, 2))

ml_risk = ml_risk_prediction(0.8, 0.6)

print("ML Risk Prediction:", ml_risk)

updated_risk = update_risk(0.5, ml_risk, 0.7)

print("Updated Risk:", updated_risk)

detection = detection_probability(1.2, updated_risk, 0.8, 0.5)

print("Detection Probability:", detection)