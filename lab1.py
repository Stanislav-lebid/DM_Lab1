class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_algorithm(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Ребра у побудованому дереві:")
        for u, v, weight in result:
            minimum_cost += weight
            print(f"{u} -- {v} == {weight}")

        print(f"Мінімальна вага остового дерева: {minimum_cost}")


def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        vertices = int(file.readline().strip())
        graph = Graph(vertices)
        for i in range(vertices):
            line = list(map(int, file.readline().split()))
            for j in range(vertices):
                if line[j] != 0:
                    graph.add_edge(i, j, line[j])
    return graph


file_name = "file.txt"
graph = read_graph_from_file(file_name)
graph.kruskal_algorithm()
