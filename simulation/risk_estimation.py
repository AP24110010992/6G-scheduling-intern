import random
from iot_network import create_iot_network

# Create network
G = create_iot_network()

print("Risk Estimation")
print("-" * 30)

for node in G.nodes():

    vulnerability = G.nodes[node]["vulnerability"]

    # Simulated ML risk score
    estimated_risk = round(
        (0.7 * vulnerability) +
        (0.3 * random.uniform(0.1, 1.0)),
        2
    )

    G.nodes[node]["risk_score"] = estimated_risk

# Show first 10 nodes
count = 0

for node, data in G.nodes(data=True):

    print(
        f"Node {node} | "
        f"Vulnerability: {data['vulnerability']} | "
        f"Risk Score: {data['risk_score']}"
    )

    count += 1

    if count == 10:
        break