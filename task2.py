import networkx as nx

# Створення графу
G = nx.Graph()
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
    ("E", "F"),
    ("F", "G")
]
G.add_edges_from(edges)

# DFS
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
            result = dfs(graph, neighbor, goal, path.copy(), visited)
            if result:
                return result
    return None

# BFS
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Порівняння результатів
start_node = "A"
goal_node = "F"

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"DFS шлях: {dfs_path}")
print(f"BFS шлях: {bfs_path}")

# Висновки
if dfs_path and bfs_path:
    print("\nВисновки:")
    print("DFS відвідує сусідні вузли якомога глибше перед переходом до інших.")
    print("BFS відвідує вузли пошарово, гарантуючи, що знайдений шлях має мінімальну кількість кроків.")
    print("У цьому графі BFS надає коротший шлях, тоді як DFS може знайти більш довгий, залежно від порядку обходу.")
