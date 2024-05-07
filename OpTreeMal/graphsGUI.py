import time
import networkx as nx
import matplotlib.pyplot as plt
import AlgorithmFunction as AlgorithmFunction
from networkx.drawing.nx_agraph import graphviz_layout


def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color=["r" if n == node else "g" for n in G.nodes],
        )
        plt.draw()
        plt.pause(0.5)
    plt.show()

    time.sleep(0.5)


G = nx.Graph()
G.add_edges_from(
    [("A", "B"), ("A", "C"), ("B", "D"), ("A", "B"), ("B", "E"), ("C", "F"), ("C", "G")]
)
pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

visualize_search(AlgorithmFunction.order_bfs(G, "A"), "BFS Visualization", G, pos)
