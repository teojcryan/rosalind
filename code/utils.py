class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes if nodes else []
        self.edges = edges if edges else {}

    def add_edge(self, u, v):
        # For undirected graphs
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)
        if v not in self.edges:
            self.edges[v] = []
        self.edges[v].append(u)
        return self

    def add_directed_edge(self, u, v):
        # For directed graphs
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)
        return self

    def generate_from_edge_list_file(self, file_path, directed=False):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            n, m = map(int, lines[0].split())
            self.nodes = list(range(1, n + 1))
            for line in lines[1:]:
                u, v = map(int, line.split())
                if directed:
                    self.add_directed_edge(u, v)
                else:
                    self.add_edge(u, v)
        return self