# simulation/full_system_demo.py

import os
import csv
import random
# Read random seed from environment (default = 42)
SEED = int(os.getenv("SIM_SEED", "42"))

random.seed(SEED)
from iot_network import create_iot_network

from attack_engine import (
    attack_random,
    attack_targeted,
    attack_burst
)

from defender_engine import (
    select_monitor_nodes,
    defend_network,
    network_stats
)

from infection_spread import spread_infection

from mlp_defender import (
    predict_attack_probability,
    encoder
)

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

ROUNDS = 100

os.makedirs("results", exist_ok=True)

# -------------------------------------------------------
# Create IoT Network
# -------------------------------------------------------

NETWORK_SIZE = 50

G = create_iot_network(
    num_nodes=NETWORK_SIZE,
    seed=SEED
)

# -------------------------------------------------------
# Initial Infection
# -------------------------------------------------------

first_infected = random.choice(list(G.nodes()))
G.nodes[first_infected]["status"] = "infected"

print("=" * 65)
print(f" FULL IoT SECURITY DEMONSTRATION ({NETWORK_SIZE} Nodes)")
print("=" * 65)

print(f"\nInitial infected device : {first_infected}\n")

results = []

# =======================================================
# Simulation Loop
# =======================================================

for round_no in range(1, ROUNDS + 1):

    # ---------------------------------------------------
    # 1. ATTACK PHASE
    # ---------------------------------------------------

    if round_no % 15 == 0:

        attack_burst(G, round_no)

    elif round_no % 5 == 0:

        attack_targeted(G, round_no)

    else:

        attack_random(G, round_no)

 # ---------------------------------------------------
# 2. Select monitored nodes first
# ---------------------------------------------------

monitored = select_monitor_nodes(G)

# ---------------------------------------------------
# 3. MLP Risk Estimation
# ---------------------------------------------------

for node in monitored:

    protocol = random.choice(list(encoder.classes_))

    probability = predict_attack_probability(
        duration=random.uniform(0.5, 5.0),
        protocol=protocol,
        sbytes=random.randint(100, 1500),
        dbytes=random.randint(50, 1200)
    )

    if probability > 0.80:

        G.nodes[node]["risk_score"] = min(
            1.0,
            G.nodes[node]["risk_score"] + 0.10
        )

    elif probability > 0.60:

        G.nodes[node]["risk_score"] = min(
            1.0,
            G.nodes[node]["risk_score"] + 0.05
        )
    # ---------------------------------------------------
    # 3. UPDATE NODE STATES
    # ---------------------------------------------------

    for node in G.nodes():

        risk = G.nodes[node]["risk_score"]

        if (
            risk >= 0.85
            and G.nodes[node]["status"] == "normal"
        ):
            G.nodes[node]["status"] = "compromised"


    # ---------------------------------------------------
    # 4. INFECTION SPREAD
    # ---------------------------------------------------

    newly_infected = spread_infection(G)

    # ---------------------------------------------------
    # 5. DEFENDER
    # ---------------------------------------------------

    recovered = defend_network(G, monitored)

    # Protected devices slowly become normal again

    for node in G.nodes():

        if G.nodes[node]["status"] == "protected":

            if random.random() < 0.20:

                G.nodes[node]["status"] = "normal"

    # ---------------------------------------------------
    # 6. CLEANUP
    # ---------------------------------------------------

    for node in G.nodes():

        if (
            G.nodes[node]["status"] == "infected"
            and G.nodes[node]["risk_score"] < 0.35
        ):
            G.nodes[node]["status"] = "normal"

    # ---------------------------------------------------
    # 7. STATISTICS
    # ---------------------------------------------------

    stats = network_stats(G)

    infected_nodes = sum(

        1

        for node in G.nodes()

        if G.nodes[node]["status"] == "infected"

    )

    results.append([

        round_no,

        stats["avg_risk"],

        stats["compromised_ratio"],

        stats["protected_nodes"],

        newly_infected,

        recovered

    ])

    print(

        f"Round {round_no:3d}"

        f" | Risk={stats['avg_risk']:.3f}"

        f" | Compromised={stats['compromised_ratio']:.3f}"

        f" | Protected={stats['protected_nodes']}"

        f" | Infected={infected_nodes}"

        f" | New={newly_infected}"

        f" | Recovered={recovered}"

    )

# =======================================================
# SAVE RESULTS
# =======================================================

csv_path = f"results/scalability_{NETWORK_SIZE}.csv"

with open(csv_path, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([

        "Round",

        "Average Risk",

        "Compromised Ratio",

        "Protected Nodes",

        "New Infections",

        "Recovered Nodes"

    ])

    writer.writerows(results)

# =======================================================
# FINAL SUMMARY
# =======================================================

final = network_stats(G)

print("\n" + "=" * 65)
print("FINAL SUMMARY")
print("=" * 65)

print(f"Rounds Executed      : {ROUNDS}")
print(f"Network Size         : {NETWORK_SIZE}")
print(f"Average Risk         : {final['avg_risk']:.3f}")
print(f"Compromised Ratio    : {final['compromised_ratio']:.3f}")
print(f"Protected Nodes      : {final['protected_nodes']}")

print("\nResults saved to:")
print(csv_path)

print("\nSimulation Complete.")