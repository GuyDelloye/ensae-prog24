from grid import Grid
from graph import Graph
from itertools import permutations

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



def apply_bfs_to_grid(g):
    gra = graph_from_grid(g)
    dico =[0 for i in range(gra.nb_nodes)]
    for k in range(len(dico)):
        dico[k] = gra.nodes[k]
    print("dico :", dico)

    def index(node):
            for i in range(len(dico)):
                if dico[i] == node:
                    return i
    
    gra_renumbered = Graph([i for i in range(len(dico))])
    for edge in gra.edges:
        n1, n2 = edge
        Graph.add_edge(gra_renumbered, index(n1), index(n2))
    #print("gra :", gra)
    #print("gra_renumbered :", gra_renumbered)
    src = index(int(Grid.grid_to_string(g)))
    dst = index(min(dico))
    print(dico[dst], dst)
    b = Graph.bfs(gra_renumbered, src, dst)
    print(b)
    for k in range(len(b)):
        b[k] = dico[k]
    return b


g = Grid(2, 2)
print(g)
print(Grid.neighbor_grids(g))


"""
g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
print("Initial:", g)

g = Grid.swap(g, (0,0), (0,1))
print("After swap: ", g)


g = Grid.swap_seq(g, [((0,0),(1,0)),((1,0),(1,1))])
print("After swap_freq: ", g)


print("is_sorted test:")
g = Grid.is_sorted(g)
print(g)


graph1 = Graph.graph_from_file("ensae-prog24/input/graph1.in")
print(graph1)

print(Graph.bfs(graph1, 1, 2))
print(Graph.bfs(graph1, 1, 3))

graph2 = Graph.graph_from_file("ensae-prog24/input/graph2.in")
print(graph2)
print(Graph.bfs(graph2, 1, 8))

print("Permut :", list(permutations('543')))


gra0 = Graph([1,2,3,4])
Graph.add_edge(gra0,1,2)
Graph.add_edge(gra0,2,3)
Graph.add_edge(gra0,3,4)
print(gra0)

print(Graph.is_connected(gra0, 1, 2))
print(Graph.is_connected(gra0, 1, 3))


print(g)
print(graph_from_grid(g))
"""