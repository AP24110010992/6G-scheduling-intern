# simulation/iot_network.py
# ---------------------------------------------------------
# 50-Node IoT Network Generator
# Summer Research Internship
# ---------------------------------------------------------

import networkx as nx
import matplotlib.pyplot as plt
import random
import os

random.seed(42)

os.makedirs("results", exist_ok=True)


def create_iot_network(num_nodes=50, seed=42):
    """
    Creates a Barabasi-Albert scale-free IoT network.
    """

    G = nx.barabasi_albert_graph(
        n=num_nodes,
        m=2,
        seed=seed
    )

    # Rename nodes
    mapping = {
        i: f"Device{i+1}"
        for i in range(num_nodes)
    }

    G = nx.relabel_nodes(G, mapping)

    # Assign attributes
    for node in G.nodes():

        G.nodes[node]["risk_score"] = round(
            random.uniform(0.1, 0.9), 2
        )

        G.nodes[node]["vulnerability"] = round(
            random.uniform(0.1, 0.9), 2
        )

        G.nodes[node]["status"] = "normal"

        G.nodes[node]["packets_sent"] = 0

    return G


def network_summary(G):

    print("=" * 45)
    print("IoT Network Summary")
    print("=" * 45)

    print("Nodes :", G.number_of_nodes())
    print("Edges :", G.number_of_edges())
    print("Density :", round(nx.density(G), 4))
    print("Connected :", nx.is_connected(G))

    print("\nSample Devices\n")

    for node in list(G.nodes())[:5]:

        print(
            node,
            G.nodes[node]
        )


def visualize_network(
    G,
    path="results/network.png"
):

    pos = nx.spring_layout(
        G,
        seed=42
    )

    colors = []

    sizes = []

    for node in G.nodes():

        risk = G.nodes[node]["risk_score"]

        if risk < 0.35:
            colors.append("green")

        elif risk < 0.70:
            colors.append("yellow")

        else:
            colors.append("red")

        sizes.append(
            200 + 40 * G.degree(node)
        )

    plt.figure(figsize=(12, 9))

    nx.draw_networkx_edges(
        G,
        pos,
        alpha=0.3
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=colors,
        node_size=sizes
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=6
    )

    plt.title("50-Node IoT Network")

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(path, dpi=150)

    plt.close()

    print(f"\nSaved: {path}")


if __name__ == "__main__":

    G = create_iot_network()

    network_summary(G)

    visualize_network(G)