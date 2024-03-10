"""
This is the graph module. It contains a minimalistic Graph class.
"""
import heapq

class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"
    
    def is_connected(self, n1, n2):
        """
        Returns whether nodes n1 and n2 are connected
        """
        return (((n1,n2) in self.edges) or ((n2,n1) in self.edges))

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

def bfs(self, src, dst):
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        queue = [src]
        visited = [False for i in range(self.nb_nodes+1)] #noeuds numérotés à partir de 1 et non 0
        visited[src] = True
        path = [[] for i in range(self.nb_nodes+1)]
        path[src] = [src]
        while queue != []:
            node = queue.pop(0)
            for nghbr in self.graph[node]:
                if not visited[nghbr]:
                    path[nghbr] = path[node] + [nghbr]
                    queue.append(nghbr)
                    visited[nghbr] = True
        return path[dst]

def bfs_old(self, src, dst):
    """
    Finds a shortest path from src to dst by BFS.  

    Parameters: 
    -----------
    src: NodeType
        The source node.
    dst: NodeType
        The destination node.

    Output: 
    -------
    path: list[NodeType] | None
        The shortest path from src to dst. Returns None if dst is not reachable from src
    """ 
    queue = [src]
    visited = [False for i in range(self.nb_nodes+1)] #noeuds numérotés à partir de 1 et non 0
    visited[src] = True
    path = [[] for i in range(self.nb_nodes+1)]
    path[src] = [src]
    while queue != []:
        node = queue.pop(0)
        for nghbr in self.graph[node]:
            if not visited[nghbr]:
                path[nghbr] = path[node] + [nghbr]
                queue.append(nghbr)
                visited[nghbr] = True
    return path[dst]
    
    def distance(node_tup):
        dist = 0
        for k in range(len(node_tup)):
            if node_tup[k] != k+1:
                dist += 1
        return dist//2
    
    def distance_old(node_int):
        l = str(node_int)
        dist = 0
        for k in range(len(l)):
            if l[k] != k+1:
                dist += 1
        return dist//2

    def distance2_old_with_int(node_int, nb_columns, nb_lines):
        l = str(node_int)
        dist = 0
        for k in range(len(l)):
            dist_k = 0
            after_swaps = l[k]
            while after_swaps != k+1:
                if after_swaps <= k+1-nb_columns:
                    after_swaps += k+1-nb_columns
                    dist_k += 1
                elif after_swaps >= k+1+nb_columns:
                    after_swaps -= k+1-nb_columns
                    dist_k += 1
                if after_swaps%nb_columns < k+1%nb_columns:
                    after_swaps += 1
                    dist_k += 1
                elif after_swaps%nb_columns > k+1%nb_columns:
                    after_swaps -= 1
                    dist_k += 1
            if dist_k > dist:
                dist = dist_k
        return dist

    def exists_inf(node, cost, li):
        for k in range(len(li)):
            h1, n1, c1 = li[k]
            if c1 < cost and n1 == node:
                return True
        return False
    
    def a_star(gra, src, dst):
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

    def a_star_old(self, src, dst):
        """
        Finds a shortest path from src to dst by A-star algorithm.
        """
        closed = {}
        open_list = []
        heapq.heappush(open_list, (Graph.distance(src), src, 0))
        if dst == src:
            return [src]
        #if dst in self.graph[src]:
            #return [src, dst]
        prec_node = src
        closed[prec_node] = []
        compteur = 0
        while open_list != []:
            compteur += 1
            heuristic, node, cost = heapq.heappop(open_list)
            if node == dst:
                return closed[prec_node] + [node]
            for nghbr in self.graph[node]:
                cost = cost + 1
                if (nghbr not in closed) and (not Graph.exists_inf(nghbr, cost, open_list)):
                    heapq.heappush(open_list, (cost + Graph.distance(nghbr), nghbr, cost))
            closed[node] = closed[prec_node] + [node]
            prec_node = node
            if compteur <= 3:
                print(compteur, 'open = ', open_list, 'closed = ', closed)
            else:
                return (compteur, 'open = ', open_list, 'closed = ', closed)
        raise Exception('No path')


    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters: 
        -----------
        file_name: str
            The name of the file

        Outputs: 
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph

