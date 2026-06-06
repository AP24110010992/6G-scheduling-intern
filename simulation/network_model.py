import networkx as nx
import matplotlib.pyplot as plt

# create empty network
network = nx.Graph()

# connect devices
network.add_edge("Node1", "Node2")
network.add_edge("Node1", "Node3")
network.add_edge("Node2", "Node4")
network.add_edge("Node3", "Node5")
network.add_edge("Node4", "Node5")

# set graph size
plt.figure(figsize=(7, 5))

# display network
nx.draw(
    network,
    with_labels=True,
    node_size=2500,
    width=2
)

# title
plt.title("IoT Network Graph")

# save graph image
plt.savefig("iot_network.png")

# show graph
plt.show()

# print details
total_nodes = network.number_of_nodes()
total_edges = network.number_of_edges()

print("Total Nodes =", total_nodes)
print("Total Connections =", total_edges)