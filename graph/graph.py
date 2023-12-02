from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from dsu import DSU


def parse_edge_default(edge) -> tuple[int, int, int]:
    if len(edge) == 2:
        u, v = edge
        weight = 1
    elif len(edge) == 3:
        u, v, weight = edge
    else:
        raise ValueError('Cannot parse the edge')
    return u, v, weight


class Graph:
    def __init__(self, n: int, edges: Iterable[tuple | list], directed=False, parse_edge=parse_edge_default):
        self.neighbours: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        self.directed: bool = directed
        self.edges_length = 0
        for edge in edges:
            u, v, weight = parse_edge(edge)
            self.neighbours[u].append((v, weight))
            if not directed:
                self.neighbours[v].append((u, weight))
            self.edges_length += 1

    def __getitem__(self, node) -> list[tuple[int, int]]:
        return self.neighbours[node]

    def __len__(self):
        return len(self.neighbours)


class Tree(Graph):
    def __init__(self, root: int, edges: list[tuple | list], directed=False, parse_edge=parse_edge_default):
        super().__init__(len(edges) + 1, edges, directed, parse_edge)
        self.root = root
        self.parents: list[int] = [-1] * len(self)
        self.depths: list[int] = [-1] * len(self)
        self._find_roots(self.root, -1, 0)

    def _find_roots(self, node: int, parent: int, depth: int):
        self.parents[node] = parent
        self.depths[node] = depth

        for neighbour, weight in self[node]:
            if neighbour == parent:
                continue
            self._find_roots(neighbour, node, depth + 1)

    def children(self, node):
        parent = self.parents[node]
        for neighbour, weight in self[node]:
            if neighbour != parent:
                yield neighbour, weight

    def find_lca(self, u, v):
        while self.depths[u] > self.depths[v]:
            u = self.parents[u]

        while self.depths[v] > self.depths[u]:
            v = self.parents[v]

        while v != u:
            v = self.parents[v]
            u = self.parents[u]

        return u

    def find_lca_by_queries(self, queries: Iterable[tuple[int, int] | list]) -> list[int]:
        pairs: list[list[tuple[int, int]]] = [[] for _ in range(len(self))]
        queries_length = 0
        for i, (u, v) in enumerate(queries):
            pairs[u].append((v, i))
            pairs[v].append((u, i))
            queries_length += 1

        dsu = DSU(len(self))
        visited = [False] * len(self)
        result = [-1] * queries_length

        def lca_dfs(node: int):
            visited[node] = True

            for pair, index in pairs[node]:
                if visited[pair]:
                    result[index] = dsu.find(pair)

            for child, _ in self.children(node):
                lca_dfs(child)

            if self.parents[node] != -1:
                dsu.join(self.parents[node], node)

        lca_dfs(self.root)

        return result
