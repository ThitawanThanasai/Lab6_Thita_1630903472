"""
Exercise(s)***ข้อนี้ขออนุญาติทำรวมนะคะ***
Requirement
- Adjacency matrix
- Adjacency list
- Edge list
"""


# Matrix
class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = 1
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = 1
            return True
        else:
            return False

    def print_graph(self):
        print('  ', end='')
        for i in sorted(self.edge_indices.keys()):
            print(i, end=' ')
        print()
        print()

        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')
            print(' ')
            print()

    def disconnect(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = 0
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = 0
            return True
        else:
            False

    def print_edge_list(self, edges):
        count = 0
        for u, v in edges:
            print("Edge list [" + str(count) + "]:", u + v)
            count += 1


"""============================================================================="""


# List
class Vertex2:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph2:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex2) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, "|", str("".join(self.vertices[key].neighbors)))

    def disconnect(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].neighbors.remove(v)
            self.vertices[v].neighbors.remove(u)
            return True
        else:
            return False

    def print_edge_list(self):
        for key in sorted(list(self.vertices.keys())):
            for neighbor in self.vertices[key].neighbors:
                print(key + ' ' + neighbor)


print("---------------------")
print("EX:1 Adjacency Matrix")
print("---------------------")

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('E')):
    g.add_vertex(Vertex(chr(i)))
edges = ['AB', 'AC', 'BC', 'CD']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
g.print_graph()

print("---------------------")
print("EX:1 Adjacency List")
print("---------------------")
g2 = Graph2()
a = Vertex2('A')
g2.add_vertex(a)
g2.add_vertex(Vertex2('B'))
for i in range(ord('A'), ord('E')):
    g2.add_vertex(Vertex2(chr(i)))
edges = ['AB', 'AC', 'BC', 'CD']
for edge in edges:
    g2.add_edge(edge[:1], edge[1:])
g2.print_graph()

print("---------------------")
print("EX:1 Edge list")
print("---------------------")
g.print_edge_list(edges)
print()
print("---------------------")
print("EX:2 Adjacency matrix")
print("---------------------")
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('G')):
    g.add_vertex(Vertex(chr(i)))
edges = ['AB', 'AC', 'AF', 'CD', 'DE', 'EF']
for edge in edges:
    g.add_edge(edge[0], edge[1])
g.print_graph()
print("---------------------")
print("EX:2 Adjacency list")
print("---------------------")
g2 = Graph2()
a = Vertex2('A')
g2.add_vertex(a)
g2.add_vertex(Vertex2('B'))
for i in range(ord('A'), ord('G')):
    g2.add_vertex(Vertex2(chr(i)))
edges = ['AB', 'AC', 'AF', 'CD', 'DE', 'FE']
for edge in edges:
    g2.add_edge(edge[:1], edge[1:])
g2.print_graph()
print("---------------------")
print("Edge list of Exercise 2")
print("---------------------")
g.print_edge_list(edges)
print()

print("---------------------")
print("EX:3 Adjacency matrix")
print("---------------------")
print("Connect AB, AC, CD, CF, EF")
print()
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('G')):
    g.add_vertex(Vertex(chr(i)))
edges = ['AB', 'AC', 'CD', 'CF', 'EF']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
g.print_graph()
print("---------------------")
print("EX:3 Adjacency list")
print("---------------------")
g2 = Graph2()
a = Vertex2('A')
g2.add_vertex(a)
g2.add_vertex(Vertex2('B'))
for i in range(ord('A'), ord('G')):
    g2.add_vertex(Vertex2(chr(i)))
edges = ['AB', 'AC', 'CD', 'CF', 'EF']
for edge in edges:
    g2.add_edge(edge[:1], edge[1:])
g2.print_graph()
print("---------------------")
print("EX:3 Edge list")
print("---------------------")
g.print_edge_list(edges)
print()
print("Disconnect CF,AB,CD")
g.disconnect('C', 'F')
g.disconnect('A', 'B')
g.disconnect('C', 'D')
edges = ['AC', 'EF']
print("---------------------")
print("EX:3 Adjacency matrix")
print("---------------------")
g.print_graph()
print("---------------------")
print("EX:3 Adjacency list")
print("---------------------")
g2.disconnect('C', 'F')
g2.disconnect('A', 'B')
g2.disconnect('C', 'D')
g2.print_graph()
print("---------------------")
print("EX:3 Edge list")
print("---------------------")
g.print_edge_list(edges)











