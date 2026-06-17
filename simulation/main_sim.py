import random
import csv
from iot_network import create_iot_network

# Create IoT network
G = create_iot_network()

# Number of simulation rounds
total_rounds = 100

# Defender monitors 5 random nodes
monitored_nodes = random.sample(list(G.nodes()), 5)

print("Monitored Nodes:")
print(monitored_nodes)
print()

# Counters
detected_attacks = 0
successful_attacks = 0
missed_attacks = 0

# Store attack logs
attack_logs = []

# Run simulation
for round_number in range(total_rounds):

    # Attacker selects the node with highest vulnerability
    target_node = max(
        G.nodes(),
        key=lambda node: G.nodes[node]["vulnerability"]
    )

    vulnerability = G.nodes[target_node]["vulnerability"]

    # Basic detection probability
    detection_probability = 1 - vulnerability

    # Increase detection chance if node is monitored
    if target_node in monitored_nodes:

        detection_probability = min(
            0.9,
            detection_probability + 0.3
        )

    # Decide attack outcome
    if random.random() < detection_probability:

        outcome = "Detected"
        detected_attacks += 1

    else:

        outcome = "Successful"
        successful_attacks += 1

        G.nodes[target_node]["status"] = "compromised"

    # Save log
    attack_logs.append([
        round_number,
        target_node,
        vulnerability,
        outcome
    ])


# Save logs to CSV file
with open("results/attack_logs.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Round",
        "Target Node",
        "Vulnerability",
        "Outcome"
    ])

    writer.writerows(attack_logs)


# Print results
print("Simulation Finished")
print()

print("Total Rounds       :", total_rounds)
print("Detected Attacks   :", detected_attacks)
print("Successful Attacks :", successful_attacks)
print("Missed Attacks     :", missed_attacks)

print()
print("Attack logs saved to results/attack_logs.csv")