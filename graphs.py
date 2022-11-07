class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.biggest_node = 0

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        if new_node.value > self.biggest_node:
            self.biggest_node = new_node.value
        self.nodes.append(new_node)
        return new_node
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = self.insert_node(node_from_val)
        if to_found == None:
            to_found = self.insert_node(node_to_val)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        # edges = []
        # for edge in self.edges:
        #     edges.append((edge.value, edge.node_from.value, edge.node_to.value))
        # return edges
        return [(e.value, e.node_from.value, e.node_to.value) for e in self.edges]

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        current_index = 0
        adjacency_list = []
        edges = self.get_edge_list()
        while current_index <= self.biggest_node:
            adjacency = None
            for x, y, z in edges:
                if current_index == y:
                    if adjacency is None:
                        adjacency = []
                    adjacency.append((z, x))
            adjacency_list.append(adjacency)
            current_index += 1
        return adjacency_list
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        adjacency_matrix = []
        adjacency_list = self.get_adjacency_list()
        for adjacency in adjacency_list:
            matrix = []
            i = 0
            while i < len(adjacency_list):
                edge_val = 0
                if adjacency is not None:
                    for node, edge in adjacency:
                        if i == node:
                            edge_val = edge
                matrix.append(edge_val)
                i += 1
            adjacency_matrix.append(matrix)
        return adjacency_matrix
    
    # uses a stack DS
    def depth_first_traversal(self):
        pass
    
    # uses a queue DS
    def breathe_first_traversal(self):
        pass

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())

