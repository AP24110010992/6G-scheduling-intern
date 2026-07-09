# Core Results

## Project
Adaptive IoT Security using Machine Learning and Deep Reinforcement Learning

---

## Objective

Develop an intelligent IoT security framework that combines:

- Machine Learning based risk prediction
- Reinforcement Learning based defence
- Dynamic attack simulation
- Infection spread modelling

---

## Components

### IoT Network
- 50 IoT devices
- Barabási–Albert topology
- Risk score assigned to every device

### Attack Engine
Three attack strategies were implemented:

- Random Attack
- Targeted Attack
- Burst Attack

### MLP Risk Prediction

A trained Multi-Layer Perceptron predicts attack probability using network traffic features.

### Infection Spread

Compromised devices propagate attacks to neighbouring devices.

### DRL Defender

A DQN agent monitors high-risk devices and protects compromised nodes.

---

## Final Results

Simulation Rounds: 100

Average Risk Score:
0.585

Compromised Ratio:
0.620

Protected Nodes:
8

---

## Conclusion

The integrated IoT security framework successfully combines machine learning, reinforcement learning, and graph-based attack simulation.

The attack engine increases device risk and propagates infections, while the defender continuously monitors high-risk devices and recovers compromised nodes. The final results demonstrate realistic interactions between attackers and defenders within the IoT network.