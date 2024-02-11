""
from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "ensae-prog24/input/"
file_name = data_path + "grid0.in"

print(file_name)
""
g = Grid.grid_from_file(file_name)
print("Initial:", g)

g = Grid.swap(g, (0,0), (0,1))
print("After swap: ", g)

""
g = Grid.swap_seq(g, [((0,0),(1,0)),((1,0),(1,1))])
print("After swap_freq: ", g)

"""
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
""
from itertools import permutations

print("Permut :", list(permutations('543')))

""
def graph_from_grid(g):
    n, m = g.n, g.m
    li = list(permutations(Grid.grid_to_string(g)))
    for k in range(len(li)):
        st = ''
        for char in li[k]:
            st += char
        li[k] = int(st)
    gra = Graph(li)
    for gri_int in li:
        gri = Grid.int_to_grid(gri_int,n,m)
        for nghbr in Grid.neighbor_grids(gri):
            nbr_int = int(nghbr)
            if not Graph.is_connected(gra, gri_int, nbr_int):
                Graph.add_edge(gra, gri_int, nbr_int)
    return gra

"""
gra0 = Graph([1,2,3,4])
Graph.add_edge(gra0,1,2)
Graph.add_edge(gra0,2,3)
Graph.add_edge(gra0,3,4)
print(gra0)
"""

print(g)
print(graph_from_grid(g))

"""
print(gra0, gra0.edges)
print(Graph.is_connected(gra0, 1, 2))
print(Graph.is_connected(gra0, 1, 3))
"""