import networkx as nx

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

# Алгоритм DFS
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result

    path.pop()
    return None

# Алгоритм BFS
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph.neighbors(current):
            if neighbor not in visited and neighbor not in [p[0] for p in queue]:
                queue.append((neighbor, path + [neighbor]))
    return None

# Порівняння шляхів
start_node = "A"
goal_node = "F"

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"Шлях DFS: {dfs_path}")
print(f"Шлях BFS: {bfs_path}")
