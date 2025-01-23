import heapq
import networkx as nx

# Алгоритм Дейкстри
def dijkstra(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == goal:
            break

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Відновлення шляху
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return distances[goal], path

# Додавання ваг у граф
G = nx.Graph()
edges_with_weights = [
    ("A", "B", 7),
    ("A", "C", 9),
    ("B", "D", 5),
    ("C", "D", 2),
    ("C", "E", 6),
    ("D", "E", 4),
    ("E", "F", 8),
    ("F", "G", 10)
]
G.add_weighted_edges_from(edges_with_weights)

# Виклик алгоритму
start_node = "A"
goal_node = "F"

shortest_distance, shortest_path = dijkstra(G, start_node, goal_node)

print(f"Найкоротший шлях від {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_distance}")
