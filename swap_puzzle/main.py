from grid import Grid
from graph import Graph
from itertools import permutations
import heapq






def graph_from_grid(g):
    """
    Build the adjacence graph of the g grid using the neighbor_grids function
    """
    n, m = g.n, g.m
    li = list(permutations(Grid.grid_to_tuple(g)))
    gra = Graph(li)
    for gri_tup in li:
        gri = Grid.tup_to_grid(gri_tup,n,m)
        for nghbr in Grid.neighbor_grids(gri):
            if not Graph.is_connected(gra, gri_tup, nghbr):
                Graph.add_edge(gra, gri_tup, nghbr)
    return gra



def graph_from_grid_old_with_int(g):
    """
    Build the adjacence graph of the g grid using the neighbor_grids function
    """
    n, m = g.n, g.m
    li = list(permutations(Grid.grid_to_string(g)))
    for k in range(len(li)):
        st = ''
        for char in li[k]:
            st += char
        li[k] = int(st)
    gra = Graph(li)
    print(li)
    for gri_int in li:
        print(gri_int)
        gri = Grid.int_to_grid(gri_int,n,m)
        for nghbr in Grid.neighbor_grids(gri):
            nbr_int = int(nghbr)
            if not Graph.is_connected(gra, gri_int, nbr_int):
                Graph.add_edge(gra, gri_int, nbr_int)
    return gra


def apply_bfs_to_grid(g):
    """
    Returns the list of the optimal swaps to solve the g grid
    """
    gra = graph_from_grid(g)
    src = Grid.grid_to_tuple(g)
    total_nodes = g.n * g.m
    dst = tuple(i for i in range(1, total_nodes+1))
    return Graph.bfs(gra, src, dst)


def apply_bfs_to_grid_old_with_int(g):
    """
    Returns the list of the optimal swaps to solve the g grid
    """
    gra = graph_from_grid(g)
    dico =[0 for i in range(gra.nb_nodes)]
    for k in range(len(dico)):
        dico[k] = gra.nodes[k]
    #print("dico :", dico)

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
    #print(dico[dst], dst)
    b = Graph.bfs(gra_renumbered, src, dst)
    #print(b)
    for k in range(len(b)):
        b[k] = dico[b[k]]
    return b



#Test BFS: it worked with the int version
g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
path = apply_bfs_to_grid(g)
print(path)




def a_star_remis_dans_classe_Graph(gra, src, dst, n, m):
        """
        Finds a shortest path in Graph gra from src to dst by A-star algorithm.
        """
        closed = {}
        prec_nodes = {}
        open_list = []
        heapq.heappush(open_list, (Graph.distance(src), src, 0))
        if dst == src:
            return [src]
        closed[src] = []
        prec_nodes[src] = src
        compteur = 0
        while open_list != []:
            compteur += 1
            heuristic, node, cost = heapq.heappop(open_list)
            if node == dst:
                return closed[prec_nodes[node]] + [node]
            for nghbr in gra.graph[node]:
                cost = cost + 1
                if (nghbr not in closed) and (not Graph.exists_inf(nghbr, cost, open_list)):
                    heapq.heappush(open_list, (cost + Graph.distance(nghbr), nghbr, cost))
                    prec_nodes[nghbr] = node
            closed[node] = closed[prec_nodes[node]] + [node]
        raise Exception('No path')

def apply_a_star_to_grid(g):
    """
    Returns the list of the optimal swaps to solve the g grid
    """
    gra = graph_from_grid(g)
    src = Grid.grid_to_tuple(g)
    total_nodes = g.n * g.m
    dst = tuple(i for i in range(1, total_nodes+1))
    return Graph.a_star(gra, src, dst)




"""
#Test A_star : OK
g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
path = apply_a_star_to_grid(g)
print(path)


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