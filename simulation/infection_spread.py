import random
from iot_network import create_iot_network

# Create IoT network
G = create_iot_network()

# Select one infected node
infected = random.choice(list(G.nodes()))

G.nodes[infected]["status"] = "infected"

print("Initially Infected Node:", infected)

# Simulate spread for 5 rounds
for round_number in range(1, 6):

    print("\nRound", round_number)

    new_infections = []

    for node in G.nodes():

        if G.nodes[node]["status"] == "infected":

            neighbours = list(G.neighbors(node))

            for neighbour in neighbours:

                if G.nodes[neighbour]["status"] == "safe":

                    # 30% chance of infection
                    if random.random() < 0.3:

                        new_infections.append(neighbour)

    # Update infections
    for node in new_infections:

        G.nodes[node]["status"] = "infected"

    infected_nodes = [
        node
        for node in G.nodes()
        if G.nodes[node]["status"] == "infected"
    ]

    print("Total Infected Devices:", len(infected_nodes))
    print("Infected Nodes:", infected_nodes)