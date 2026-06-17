import random
from iot_network import create_iot_network

# Create network
G = create_iot_network()

print("Dynamic Risk Updates")
print("-" * 30)

# Simulate 5 update rounds
for round_number in range(1, 6):

    print("\nRound", round_number)

    for node in G.nodes():

        current_risk = G.nodes[node].get("risk_score", 0.5)

        # Random increase or decrease
        change = random.uniform(-0.1, 0.1)

        new_risk = current_risk + change

        # Keep risk between 0 and 1
        new_risk = max(0.0, min(1.0, round(new_risk, 2)))

        G.nodes[node]["risk_score"] = new_risk

    # Display first 5 nodes
    count = 0

    for node, data in G.nodes(data=True):

        print(
            f"Node {node} | Risk Score: {data['risk_score']}"
        )

        count += 1

        if count == 5:
            break