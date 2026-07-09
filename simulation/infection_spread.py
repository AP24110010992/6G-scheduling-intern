import random


def spread_infection(G, infection_probability=0.15):
    """
    Spread infection from infected devices to neighbors.
    """

    new_infections = []

    for node in G.nodes():

        if G.nodes[node]["status"] in ["infected", "compromised"]:

            for neighbour in G.neighbors(node):

                if G.nodes[neighbour]["status"] == "normal":

                    if random.random() < infection_probability:

                        new_infections.append(neighbour)

    for node in new_infections:

        G.nodes[node]["status"] = "infected"

    return len(new_infections)