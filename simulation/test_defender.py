from iot_network import create_iot_network
from attack_engine import attack_targeted
from defender_engine import (
    select_monitor_nodes,
    defend_network,
    network_stats
)

G = create_iot_network()

print("Initial Statistics")
print(network_stats(G))

print()

attack_targeted(G, 1)

monitor = select_monitor_nodes(G)

print("Monitoring:")
print(monitor)

print()

detected = defend_network(G, monitor)

print("Detected:", detected)

print()

print("Final Statistics")
print(network_stats(G))