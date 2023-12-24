class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes if nodes else []
        self.edges = edges if edges else {}

    def add_edge(self, u, v, directed):
        if directed:
            if u not in self.edges:
                self.edges[u] = []
            self.edges[u].append(v)
            return self
        else:
            if u not in self.edges:
                self.edges[u] = []
            self.edges[u].append(v)
            if v not in self.edges:
                self.edges[v] = []
            self.edges[v].append(u)
            return self

    def generate_from_edge_list_file(self, file_path, directed=False):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            n, m = map(int, lines[0].split())
            self.nodes = list(range(1, n + 1))
            for line in lines[1:]:
                u, v = map(int, line.split())
                self.add_edge(u, v, directed)
        return self