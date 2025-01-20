import networkx as nx

# Створення графу
G = nx.Graph()

# Додавання вершин і ребер (транспортна мережа міста) з вагами
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

# Алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra(graph, start, goal):
    # Використовуємо бібліотеку networkx для алгоритму Дейкстри
    length, path = nx.single_source_dijkstra(graph, start)

    # Повертаємо найкоротший шлях і його довжину для заданої цілі
    return length[goal], path[goal]

# Визначення початкової та кінцевої вершин
start_node = "A"
goal_node = "F"

# Знаходимо найкоротший шлях
shortest_distance, shortest_path = dijkstra(G, start_node, goal_node)

# Виведення результату
print(f"Найкоротший шлях від {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_distance}")
