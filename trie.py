class Trie:
    __slots__ = ('root',)

    class Node:
        __slots__ = ('value', 'children', 'is_word')

        def __init__(self, value=None):
            self.value = value
            self.children = {}
            self.is_word = False

    def __init__(self, values=None):
        self.root = self.Node()
        if values is not None:
            for value in values:
                self.add(value)

    def has(self, iterable):
        node = self.root
        for value in iterable:
            node = node.children.get(value)
            if not node:
                return False
        return node.is_word

    def add(self, iterable):
        node = self.root
        for value in iterable:
            next_node = node.children.get(value)
            if not next_node:
                next_node = node.children[value] = self.Node(value)
            node = next_node
        node.is_word = True

    def iter(self, generator):
        node = self.root
        for i, value in enumerate(generator):
            node = node.children.get(value)
            if not node:
                break
            yield i, node
