import networkx as nx
import random

def create_iot_network():
    G = nx.barabasi_albert_graph(50, 3)

    for node in G.nodes():
        G.nodes[node]["vulnerability"] = round(random.uniform(0.1, 1.0), 2)
        G.nodes[node]["status"] = "safe"

    return G


if __name__ == "__main__":
    network = create_iot_network()

    print("Total Nodes:", network.number_of_nodes())
    print("Total Edges:", network.number_of_edges())

    print("\nSample Nodes:")
    count = 0

    for node, data in network.nodes(data=True):
        print(node, data)

        count += 1
        if count == 5:
            break