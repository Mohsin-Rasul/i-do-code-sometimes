def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u) # For undirected graph

# Main Program
network = {}
add_edge(network, "Main", "Oak")
add_edge(network, "Elm", "Maple")
add_edge(network, "Main", "Maple")

print("Network Vertices:", list(network.keys()))
print("Adjacency List:", network)