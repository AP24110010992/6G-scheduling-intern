import networkx as nx
import matplotlib.pyplot as plt
import random
import os

# Create results folder if it doesn't exist
os.makedirs("results", exist_ok=True)

# Create a 50-node IoT network
G = nx.barabasi_albert_graph(50, 2)

# Add device information
for node in G.nodes():
    G.nodes[node]["risk"] = round(random.uniform(0.1, 1.0), 2)
    G.nodes[node]["status"] = "safe"

# Print network summary
print("50-Node IoT Network")
print("-" * 30)
print("Total Nodes :", G.number_of_nodes())
print("Total Edges :", G.number_of_edges())

print("\nSample Device Information:")
count = 0

for node, data in G.nodes(data=True):
    print(f"Device {node}: {data}")

    count += 1
    if count == 5:
        break

# Assign colors based on risk
colors = []

for node in G.nodes():

    risk = G.nodes[node]["risk"]

    if risk < 0.4:
        colors.append("green")

    elif risk < 0.7:
        colors.append("yellow")

    else:
        colors.append("red")

# Draw network
plt.figure(figsize=(10, 8))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=500,
    font_size=7,
    edge_color="gray"
)

plt.title("50-Node IoT Network")

plt.savefig("results/50_node_network.png")

plt.show()

print("\nNetwork image saved to:")
print("results/50_node_network.png")