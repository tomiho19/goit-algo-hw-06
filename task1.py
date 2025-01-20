import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вершин і ребер (транспортна мережа міста)
edges = [
    ("A", "B", 7),
    ("A", "C", 9),
    ("B", "D", 5),
    ("C", "D", 2),
    ("C", "E", 6),
    ("D", "E", 4),
    ("E", "F", 8),
    ("F", "G", 10)
]
G.add_weighted_edges_from(edges)

# Візуалізація графу
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Середній ступінь вершин:", sum(dict(G.degree()).values()) / G.number_of_nodes())
