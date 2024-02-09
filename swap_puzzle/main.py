""
from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "ensae-prog24/input/"
file_name = data_path + "grid0.in"

print(file_name)
"""
g = Grid.grid_from_file(file_name)
print("Initial:", g)

g = Grid.swap(g, (0,0), (0,1))
print("After swap: ", g)

""
g = Grid.swap_seq(g, [((0,0),(1,0)),((1,0),(1,1))])
print("After swap_freq: ", g)

""
print("is_sorted test:")
g = Grid.is_sorted(g)
""

print("is_sorted test with the initial grid:")
g = Grid(2,3)
print(g, g.m, g.n)
g = Grid.is_sorted(g)
"""

from graph import Graph
""

data_path = "ensae-prog24/input/"
file_name = data_path + "graph1.in"

graph1 = Graph.graph_from_file(file_name)
print(graph1)

print(Graph.bfs(graph1, 1, 2))
"""
def permutations(st):


def graph_from_grid(g):
    li = permutations(Grid.grid_to_tuple(g))
    gra = Graph(li)
    for gri_tup in li:
        gri = Grid.tuple_to_grid(gri_tup)
        for nghbr in Grid.neighbor_grids(gri):
            if nghbr not in :
                Graph.add_edge(gra, gri_tup, nghbr)
    return gra
"""

g = Graph([1,2,3,4])
Graph.add_edge(g,1,2)
Graph.add_edge(g,2,3)
Graph.add_edge(g,3,4)
print(g)