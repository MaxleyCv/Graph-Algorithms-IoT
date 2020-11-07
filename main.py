import copy

INPUT_FILE = open("career.in")
OUTPUT_FILE = open("career.out")


class Graph:
    """
    Class for iplementation of the graphs
    Has a list of Vertexes, each vertex has value and maximum pathway property
    """
    def __init__(self):
        self.vertexes = []
        self.max_profit = 0

    def add_vertex(self, val, connections):
        new_vertex = Graph.Vertex(val)
        new_vertex.connections = copy.deepcopy(connections)
        self.vertexes.append(new_vertex)

    class Vertex:
        """
        Vertex of the graph, has connections that are relative for a particular graph
        (e.g. one vertex is impossible to use in two different graphs)
        """

        def __init__(self, val):
            self.value = val
            self.connections = []
            self.pathway = 0

    def get_breadth(self, index):
        current = copy.deepcopy(self.vertexes[index])
        if current.pathway > self.max_profit:
            self.max_profit = current.pathway
        if len(current.connections):
            for new_index in self.vertexes[index].connections:
                next_vertex = copy.deepcopy(self.vertexes[new_index])
                if next_vertex.pathway <= current.pathway + next_vertex.value:
                    self.vertexes[new_index].pathway = current.pathway + next_vertex.value
                    self.get_breadth(new_index)
                else:
                    continue
        else:
            return


def get_maximum_profit(hierarchy):
    """
    :param hierarchy: biased self of pyramydial hierarchy
    :return: maximum path weight
    """
    hierarchy.get_breadth(len(hierarchy.vertexes) - 1)
    return hierarchy.max_profit


def generate_indexes(level_length, index, graph):
    new_id = len(graph.vertexes) + index
    return [new_id - level_length, new_id - level_length - 1]


def get_items():
    hierarchy = Graph()
    income = INPUT_FILE.readlines()
    for i in range(len(income)):
        income[i] = str.replace(income[i], '\n', '')
    length = int(income.pop(0))
    for level in range(length):
        new_level = list(map(int, income.pop().split(' ')))
        for new_index in range(len(new_level)):
            if len(new_level) == length:
                hierarchy.add_vertex(new_level[new_index], [])
            else:
                hierarchy.add_vertex(new_level[new_index], generate_indexes(len(new_level), new_index, hierarchy))
    return hierarchy


if __name__ == "__main__":
    print(get_maximum_profit(get_items()))

