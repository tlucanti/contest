
class GraphAdjacency:
    last_edge = 0

    def __init__(self, vert):
        self.vertices = vert
        self.adjacency_matrix = [[[False,  # adjacency
                                   0,      # entry time
                                   0,      # leave time
                                   ] for i in range(vert)] for j in range(vert)]

    def add_edge(self, edge_1, edge_2):
        self.adjacency_matrix[edge_1][edge_2] = [True, -1, -1]
        self.adjacency_matrix[edge_2][edge_1] = [True, -1, -1]
        self.last_edge = edge_1

    def dfs(self, edge):
        time = 0
        for i in range(self.vertices):
            if i == edge:
                continue
            vertex = self.adjacency_matrix[edge][i]
            if vertex[0]:
                if vertex[1] == -1:
                    vertex[1] = time
                    self.dfs(i)

    def show_bridges(self):
        for i in range(self.vertices):
            
            for