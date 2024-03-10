from grid import Grid
from graph import Graph
from itertools import permutations
import heapq
import matplotlib.pyplot as plt


#First functions
g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
print("Initial:", g)

g = Grid.swap(g, (0,0), (0,1))
print("After swap: ", g)

g = Grid.swap_seq(g, [((0,0),(1,0)),((1,0),(1,1))])
print("After swap_freq: ", g)

print("is_sorted test:")
g = Grid.is_sorted(g)
print(g)


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


def apply_bfs_to_grid(g):
    """
    Returns the list of the optimal swaps to solve the g grid
    """
    gra = graph_from_grid(g)
    src = Grid.grid_to_tuple(g)
    total_nodes = g.n * g.m
    dst = tuple(i for i in range(1, total_nodes+1))
    return Graph.bfs(gra, src, dst)



#Test BFS
g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
path = apply_bfs_to_grid(g)
print(path)



def apply_a_star_to_grid(g):
    """
    Returns the list of the optimal swaps to solve the g grid
    """
    gra = graph_from_grid(g)
    src = Grid.grid_to_tuple(g)
    total_nodes = g.n * g.m
    dst = tuple(i for i in range(1, total_nodes+1))
    return Graph.a_star(gra, src, dst)

#Test A_star
g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
path = apply_a_star_to_grid(g)
print(path)



#Visualize
def visualize_grid(grid_object):
    """
    Visualize a Grid object using matplotlib
    """
    grid = grid_object.state # Access the state of the grid
    m = len(grid) # Number of rows
    n = len(grid[0]) if m > 0 else 0 # Number of columns

    fig, ax = plt.subplots()
    ax.set_xlim(0,n)
    ax.set_ylim(0,m)
    plt.gca().invert_yaxis()

    for x in range(n + 1):
        ax.axvline(x, color='black')
    for y in range(m + 1):
        ax.axhline(y, color='black')
    
    for i in range(m):
        for j in range(n):
            ax.text(j + 0.5, i + 0.5, str(grid[i][j]), va='center', ha='center')
    
    plt.xticks([])
    plt.yticks([])
    plt.show()

g = Grid.grid_from_file("ensae-prog24/input/grid0.in")
visualize_grid(g)