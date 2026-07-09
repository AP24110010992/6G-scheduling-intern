# IoT Security Simulation using Machine Learning and Reinforcement Learning

## Project Overview

This project implements an intelligent IoT security framework that simulates cyber attacks on an Industrial IoT network and evaluates multiple defense strategies. The framework combines graph-based network modeling, machine learning, deep learning, and reinforcement learning to improve network security.

The project was developed as part of a research internship on IoT Security.

---

## Features

* 50-node IoT network simulation using NetworkX
* Random, targeted, and burst attack simulation
* Defender engine for monitoring and protecting devices
* Random Forest-based attack detection
* Multi-Layer Perceptron (MLP) attack classifier
* Deep Q-Network (DQN) reinforcement learning defender
* Performance evaluation and visualization
* Modular project structure for easy extension

---

## Project Architecture

```
                IoT Network
                     │
                     ▼
             Attack Engine
                     │
                     ▼
            Defender Engine
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
Random Forest       MLP         RL (DQN)
     │               │               │
     └───────────────┼───────────────┘
                     ▼
           Performance Evaluation
```

---

## Project Structure

```
iot-security-intern/
│
├── dataset/
├── ml/
├── rl/
├── simulation/
├── results/
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* NetworkX
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* TensorFlow / Keras
* Gymnasium
* Stable-Baselines3

---

## Workflow

1. Create a 50-node IoT network.
2. Simulate cyber attacks.
3. Apply defender strategies.
4. Detect attacks using Machine Learning models.
5. Train a Reinforcement Learning agent.
6. Compare defender performance.
7. Generate performance graphs.

---

## Results

The project generates:

* Network visualization
* Average Risk vs Round
* Compromised Ratio vs Round
* Protected Nodes vs Round
* Simulation logs
* Trained ML and RL models

---

## Future Improvements

* Larger IoT networks
* Graph Neural Networks (GNNs)
* Multi-agent reinforcement learning
* Real-time streaming data
* Cloud deployment

---

## Author

Developed as part of an IoT Security Research Internship.
