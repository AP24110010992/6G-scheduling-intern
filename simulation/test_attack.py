from iot_network import create_iot_network
from attack_engine import (
    attack_random,
    attack_targeted,
    attack_burst
)

G = create_iot_network()

print(attack_random(G, 1))
print(attack_targeted(G, 2))
print(attack_burst(G, 3))