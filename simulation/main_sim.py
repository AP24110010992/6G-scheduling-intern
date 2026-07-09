# simulation/main_sim.py
# ---------------------------------------------------------
# Main IoT Security Simulation
# ---------------------------------------------------------

import csv
import os

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

os.makedirs("results", exist_ok=True)


def run_simulation(rounds=100):

    G = create_iot_network()

    logs = []

    print("=" * 50)
    print("Starting IoT Security Simulation")
    print("=" * 50)

    for t in range(1, rounds + 1):

        # Defender chooses important nodes
        monitored = select_monitor_nodes(G)

        # Attack Strategy
        if t % 15 == 0:
            attack_log = attack_burst(G, t)

        elif t % 5 == 0:
            attack_log = attack_targeted(G, t)

        else:
            attack_log = attack_random(G, t)

        # Defender reacts
        detected = defend_network(G, monitored)

        # Network statistics
        stats = network_stats(G)

        logs.append({
            "Round": t,
            "Average Risk": stats["avg_risk"],
            "Compromised Ratio": stats["compromised_ratio"],
            "Protected Nodes": stats["protected_nodes"],
            "Detected": detected
        })

        print(
            f"Round {t:3d} | "
            f"Risk={stats['avg_risk']:.3f} | "
            f"Compromised={stats['compromised_ratio']:.3f} | "
            f"Protected={stats['protected_nodes']}"
        )

    csv_file = "results/simulation_results.csv"

    with open(csv_file, "w", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=logs[0].keys())

        writer.writeheader()

        writer.writerows(logs)

    print("\nSimulation Complete")
    print(f"Results saved to {csv_file}")


if __name__ == "__main__":
    run_simulation()