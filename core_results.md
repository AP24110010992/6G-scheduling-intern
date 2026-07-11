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


## Week 6 Experimental Evaluation

### Scalability Analysis

| Network Size | Average Risk | Compromised Ratio | Protected Nodes |
|--------------|--------------|-------------------|-----------------|
| 50 Nodes | 0.585 | 0.620 | 8 |
| 100 Nodes | 0.560 | 0.710 | 7 |

### Baseline vs Proposed System

| Metric | Baseline | Proposed |
|---------|----------|----------|
| Average Risk | 0.872 | 0.574 |
| Compromised Ratio | 1.000 | 0.624 |
| Protected Nodes | 0 | 7.6 |

### Statistical Evaluation (5 Runs)

| Metric | Mean | Standard Deviation |
|---------|------|--------------------|
| Average Risk | 0.5738 | 0.0085 |
| Compromised Ratio | 0.6240 | 0.0329 |
| Protected Nodes | 7.60 | 1.52 |

### Key Findings

- The proposed MLP-assisted adaptive defense significantly outperformed the baseline approach.
- Average network risk was reduced by approximately 34%.
- The compromised ratio decreased from 100% in the baseline to approximately 62%.
- The adaptive defender protected an average of 7–8 devices per simulation.
- Scalability experiments showed the framework remained effective when the network size increased from 50 to 100 devices.