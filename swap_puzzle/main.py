"""from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "ensae-prog24/input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print("Initial:", g)

g = Grid.swap(g, (0,0), (0,1))
print("After swap: ", g)

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

graph1 = Graph.graph_from_file("../input/graph1.in")
print(graph1)

print(Graph.bfs(graph1, 1, 2))

