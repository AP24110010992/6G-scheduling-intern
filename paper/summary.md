This paper is about improving security in IoT networks using machine learning and game theory.

The authors created a smart security system that can detect and stop cyber attacks in 5G IoT networks.

The system treats the attacker and defender like players in a game. The defender tries to protect devices while the attacker tries to compromise them.

Stackelberg game theory is used so the defender can predict attacker actions and respond better.

Machine learning is used to calculate the risk level of each IoT device based on its behavior and vulnerabilities.

The IoT network is simulated using NetworkX, and SimPy is used to model attacks over time.

The framework can detect attacks, stop malware spread, and recover compromised devices.

The results show that the Stackelberg strategy performs better than Nash equilibrium by reducing attack success and improving detection rates.

The model achieved high detection accuracy with very few false alarms.

Overall,combining machine learning and game theory can create a strong and adaptive security system for future IoT networks.

Important Equations:

Defender Utility Function
Ud = αD − βC
This equation measures defender performance using detected attacks and compromised devices.
Attacker Utility Function
Ua = γC − δD
This equation represents attacker gain based on successful compromises and detection penalties.
Machine Learning Risk Prediction
RiML = f(xi)
Machine learning predicts device risk using vulnerability and historical behavior.
Risk Score Update
Ri = λRi + (1 − λ)RiML
This combines current risk and ML-predicted risk.
Detection Probability
Pdetect = 1 / (1 + e−(θ1Ri − θ2F))
This equation calculates the probability of detecting attacks.