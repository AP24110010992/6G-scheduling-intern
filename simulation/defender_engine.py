# simulation/defender_engine.py
# ---------------------------------------------------------
# Defender Engine
# Selects important devices and computes network statistics
# ---------------------------------------------------------

import random
import networkx as nx


def select_monitor_nodes(G, top_k=15):
    """
    Select the top-k highest risk nodes for monitoring.
    """

    monitored = sorted(
        G.nodes(),
        key=lambda n: G.nodes[n]["risk_score"],
        reverse=True
    )[:top_k]

    return monitored


def defend_network(G, monitored_nodes):
    """
    Defend monitored nodes.
    - Slightly reduces risk on monitored nodes.
    - Attempts to recover compromised nodes.
    """

    detected = 0

    for node in monitored_nodes:

        # Reduce risk slightly
        G.nodes[node]["risk_score"] = max(
            0.10,
            G.nodes[node]["risk_score"] - 0.05
        )

        # Recover only compromised nodes
        if G.nodes[node]["status"] in ["compromised", "infected"]:

            # 60% chance of recovery
            if random.random() < 0.85:

                G.nodes[node]["status"] = "protected"

                # Lower the risk after recovery
                G.nodes[node]["risk_score"] *= 0.65

                detected += 1

    return detected


def network_stats(G):
    """
    Compute overall network statistics.
    """

    risks = [
        G.nodes[node]["risk_score"]
        for node in G.nodes()
    ]

    compromised = sum(
        1
        for node in G.nodes()
        if G.nodes[node]["status"] in ["compromised", "infected"]
    )

    protected = sum(
        1
        for node in G.nodes()
        if G.nodes[node]["status"] == "protected"
    )

    return {
        "avg_risk": round(sum(risks) / len(risks), 3),
        "compromised_ratio": round(
            compromised / G.number_of_nodes(),
            3
        ),
        "protected_nodes": protected
    }