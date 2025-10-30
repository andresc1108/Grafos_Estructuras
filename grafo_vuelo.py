import networkx as nx
import matplotlib.pyplot as plt

# creacion del grafo
G = nx.DiGraph()

# Nodos 
airports = ["BOG", "MDE", "LIM", "SCL", "MEX"]
G.add_nodes_from(airports)

# Aristas con pesos
flights = [
    ("BOG", "MDE", 1),
    ("BOG", "LIM", 3),
    ("BOG", "MEX", 4.5),
    ("MDE", "LIM", 3.5),
    ("LIM", "SCL", 2),
    ("MEX", "LIM", 5),
    ("SCL", "BOG", 5)
]
G.add_weighted_edges_from(flights)

# Visualizacion 
pos = nx.spring_layout(G, seed=42)  # disposición estable
plt.figure(figsize=(9, 7))
plt.axis("off")

# NODOS
nx.draw_networkx_nodes(
    G, pos,
    node_color="#93C5FD",  # azul claro
    node_size=2800,
    edgecolors='black',
    linewidths=2
)

nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

nx.draw_networkx_edges(
    G, pos,
    edge_color="#111827",
    arrowstyle='-|>',
    arrowsize=20,
    width=2,
    connectionstyle="arc3,rad=0.15"
)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="darkblue", font_size=10, rotate=False)

# Ruta mas corta
route = nx.shortest_path(G, source="BOG", target="SCL", weight="weight")
time = nx.shortest_path_length(G, source="BOG", target="SCL", weight="weight")

# Mostrar la ruta mas corta en color rojo
route_edges = list(zip(route, route[1:]))
nx.draw_networkx_edges(
    G, pos,
    edgelist=route_edges,
    edge_color="red",
    width=3,
    arrows=True,
    arrowstyle='-|>',
    connectionstyle="arc3,rad=0.15"
)

plt.title(
    f"✈️ Red de Vuelos entre Aeropuertos Latinoamericanos\nRuta mas corta: {' → '.join(route)} ({time} h)",
    fontsize=13,
    fontweight="bold",
    color="#1E3A8A"
)

plt.tight_layout()
plt.show()

print("Ruta mas corta de BOG a SCL:", " → ".join(route))
print("Tiempo total de vuelo:", time, "horas")
