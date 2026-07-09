# simulation/attack_engine.py
# ---------------------------------------------------------
# Attack Engine
# Simulates different attacker strategies
# ---------------------------------------------------------

import random


def attack_random(G, round_no):
    """
    Attack a randomly selected device.
    """

    target = random.choice(list(G.nodes()))

    G.nodes[target]["risk_score"] = min(
        1.0,
        G.nodes[target]["risk_score"] + 0.25
    )

    if G.nodes[target]["risk_score"] > 0.8:
        G.nodes[target]["status"] = "compromised"

    return {
        "round": round_no,
        "mode": "random",
        "target": target
    }


def attack_targeted(G, round_no):
    """
    Attack the most vulnerable device.
    """

    target = max(
        G.nodes(),
        key=lambda n: G.nodes[n]["vulnerability"]
    )

    G.nodes[target]["risk_score"] = min(
        1.0,
        G.nodes[target]["risk_score"] + 0.35
    )

    if G.nodes[target]["risk_score"] > 0.8:
        G.nodes[target]["status"] = "compromised"

    return {
        "round": round_no,
        "mode": "targeted",
        "target": target
    }


def attack_burst(G, round_no, n=5):
    """
    Attack multiple devices simultaneously.
    """

    targets = random.sample(list(G.nodes()), n)

    logs = []

    for target in targets:

        G.nodes[target]["risk_score"] = min(
            1.0,
            G.nodes[target]["risk_score"] + 0.20
        )

        if G.nodes[target]["risk_score"] > 0.8:
            G.nodes[target]["status"] = "compromised"

        logs.append({
            "round": round_no,
            "mode": "burst",
            "target": target
        })

    return logs