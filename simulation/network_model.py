import networkx as nx
import matplotlib.pyplot as plt
import random

# Create IoT network graph
G = nx.erdos_renyi_graph(15, 0.3)

# Add device properties
for node in G.nodes():
    G.nodes[node]['risk'] = round(random.uniform(0.1, 1.0), 2)
    G.nodes[node]['state'] = "safe"

# Randomly compromise one device
infected_node = random.choice(list(G.nodes()))
G.nodes[infected_node]['state'] = "compromised"

print("Compromised Device:", infected_node)

# Display node information
for node in G.nodes(data=True):
    print(node)

# Node colors
colors = []

for node in G.nodes():
    if G.nodes[node]['state'] == "compromised":
        colors.append("red")
    else:
        colors.append("green")

# Draw graph
nx.draw(
    G,
    with_labels=True,
    node_color=colors,
    node_size=800,
    font_size=10
)

plt.title("IoT Network Simulation")
plt.show()