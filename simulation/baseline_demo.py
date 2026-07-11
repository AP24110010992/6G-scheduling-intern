import os
import csv
import random

from iot_network import create_iot_network
from attack_engine import (
    attack_random,
    attack_targeted,
    attack_burst
)
from infection_spread import spread_infection
from defender_engine import network_stats

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

ROUNDS = 100
NETWORK_SIZE = 50

SEED = int(os.getenv("SIM_SEED", "42"))
random.seed(SEED)

os.makedirs("results", exist_ok=True)

# -------------------------------------------------------
# Create IoT Network
# -------------------------------------------------------

G = create_iot_network(
    num_nodes=NETWORK_SIZE,
    seed=SEED
)

# Initial infection
first_infected = random.choice(list(G.nodes()))
G.nodes[first_infected]["status"] = "infected"

print("=" * 60)
print("BASELINE IoT SECURITY DEMO")
print("=" * 60)

results = []

for round_no in range(1, ROUNDS + 1):

    # -----------------------
    # Simple attacks only
    # -----------------------

    if round_no % 15 == 0:
        attack_burst(G, round_no)
    elif round_no % 5 == 0:
        attack_targeted(G, round_no)
    else:
        attack_random(G, round_no)

    # High-risk nodes become compromised
    for node in G.nodes():

        if (
            G.nodes[node]["risk_score"] >= 0.85
            and G.nodes[node]["status"] == "normal"
        ):
            G.nodes[node]["status"] = "infected"

    # Infection spread
    spread_infection(G)

    # Very weak defender
    for node in random.sample(list(G.nodes()), 3):

        if G.nodes[node]["status"] == "infected":

            if random.random() < 0.25:

                G.nodes[node]["status"] = "normal"

                G.nodes[node]["risk_score"] *= 0.90

    stats = network_stats(G)

    infected = sum(
        1
        for node in G.nodes()
        if G.nodes[node]["status"] == "infected"
    )

    protected = sum(
        1
        for node in G.nodes()
        if G.nodes[node]["status"] == "protected"
    )

    results.append([
        round_no,
        stats["avg_risk"],
        stats["compromised_ratio"],
        protected,
        infected
    ])

csv_path = "results/baseline_results.csv"

with open(csv_path, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Round",
        "Average Risk",
        "Compromised Ratio",
        "Protected Nodes",
        "Infected Nodes"
    ])

    writer.writerows(results)

final = network_stats(G)

print("\nFINAL SUMMARY")
print("-" * 40)

print("Average Risk      :", final["avg_risk"])
print("Compromised Ratio :", final["compromised_ratio"])
print("Protected Nodes   :", final["protected_nodes"])

print("\nSaved:", csv_path)