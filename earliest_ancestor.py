class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v_from, v_to):
        self.add_vertex(v_from)
        self.add_vertex(v_to)

        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)

    def earliest_ancestor(self, i):
        next_gen = self.vertices.get(i, set())

        if not next_gen:
            return -1

        gen = 0

        while next_gen:
            curr_gen = next_gen

            next_gen = set()

            for indiv in curr_gen:
                next_gen |= self.vertices[indiv]

        return min(curr_gen)


def earliest_ancestor(i, edges):
    g = Graph()

    for parent, child in edges:
        g.add_edge(child, parent)

    return g.earliest_ancestor(i)


if __name__ == '__main__':
    edge_inp = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (8, 9),
        (11, 8),
        (10, 1)
    ]

    assert earliest_ancestor(6, []) == -1
    assert earliest_ancestor(1, edge_inp) == 10
    assert earliest_ancestor(2, edge_inp) == -1
    assert earliest_ancestor(3, edge_inp) == 10
    assert earliest_ancestor(4, edge_inp) == -1
    assert earliest_ancestor(5, edge_inp) == 4
    assert earliest_ancestor(6, edge_inp) == 10
    assert earliest_ancestor(7, edge_inp) == 4
    assert earliest_ancestor(8, edge_inp) == 4
    assert earliest_ancestor(9, edge_inp) == 4
    assert earliest_ancestor(10, edge_inp) == -1
    assert earliest_ancestor(11, edge_inp) == -1
