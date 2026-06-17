# game_theory.py

# Defender Utility
def stackelberg_equilibrium(D, C):

    alpha = 2
    beta = 1

    Ud = (alpha * D) - (beta * C)

    return Ud


# Attacker Utility
def nash_equilibrium(C, D):

    gamma = 3
    delta = 1

    Ua = (gamma * C) - (delta * D)

    return Ua


# Sample values
detected_attacks = 8
compromised_devices = 3

defender_score = stackelberg_equilibrium(
    detected_attacks,
    compromised_devices
)

attacker_score = nash_equilibrium(
    compromised_devices,
    detected_attacks
)

print("Defender Utility =", defender_score)
print("Attacker Utility =", attacker_score)