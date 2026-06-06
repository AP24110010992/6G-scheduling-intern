import networkx as nx
import matplotlib.pyplot as plt
import random

# Create IoT network graph with 5 nodes
G = nx.erdos_renyi_graph(5, 0.4)

# Add properties to each node
for node in G.nodes():

    G.nodes[node]["risk"] = round(random.uniform(0.1, 1.0), 2)
    G.nodes[node]["state"] = "safe"

# Select one compromised device
infected_node = random.choice(list(G.nodes()))

G.nodes[infected_node]["state"] = "compromised"

print("Compromised Device :", infected_node)
print()

# Print node details
for node in G.nodes(data=True):

    print(node)

# Node colors
colors = []

for node in G.nodes():

    if G.nodes[node]["state"] == "compromised":

        colors.append("red")

    else:

        colors.append("green")

# Draw graph
plt.figure(figsize=(6, 4))

nx.draw(
    G,
    with_labels=True,
    node_color=colors,
    node_size=1200,
    font_size=10
)

plt.title("5 Node IoT Network")

# Save graph image
plt.savefig("results/iot_network.png")

plt.show()