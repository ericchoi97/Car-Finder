#Find my car in a large parking lot with graphical representation in 20x20 tile
#Start at Lower Left Corner & the Car is @ Row 10 Column 10

import networkx as nx
import matplotlib.pyplot as plt

# Parking Lot Graph
def draw_graph(graph, pos, ax, sg=None):
    # Draw Red Path
    if sg:
        nx.draw_networkx_nodes(graph, pos=pos, nodelist=sg, node_color='r', ax=ax)
        nx.draw_networkx_edges(graph, pos=pos, edgelist=graph.edges(sg), edge_color='r', ax=ax)
    else:
        nx.draw_networkx_nodes(graph, pos=pos, ax=ax)
        nx.draw_networkx_edges(graph, pos=pos, ax=ax)
    ax.set_axis_off()

# Heuristic Euclidean Distance
def heuristic(u, v):
    return ((v[0]-u[0])**2 + (v[1]-u[1])**2)**0.5

# Function A* Search
def find_car(graph, start, goal):
    path = nx.astar_path(graph, start, goal, heuristic)
    return path

# Function Plot
def plot_path(graph, start, goal, path):
    fig, ax = plt.subplots()
    pos = {i: i for i in graph.nodes()}
    draw_graph(graph, pos, ax)
    draw_graph(graph, pos, ax, sg=path)
    plt.show()

if __name__ == "__main__":
    # Generate a 10x10 grid as our "parking lot"
    G = nx.grid_graph(dim=[20, 20])
    # Define Nodes
    start_node = (1, 1)
    goal_node = (10, 10)
    # Find the Path, A* Search
    car_path = find_car(G, start_node, goal_node)
    # Print Plot
    print(car_path)
    plot_path(G, start_node, goal_node, car_path)
