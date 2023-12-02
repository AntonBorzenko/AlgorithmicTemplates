class DictDSU:
    def __init__(self):
        self.roots = {}

    def find(self, value):
        if value not in self.roots:
            return value
        if self.roots[value] != value:
            self.roots[value] = self.find(self.roots[value])
        return self.roots[value]

    def join(self, value1, value2):
        value1 = self.find(value1)
        value2 = self.find(value2)
        if value1 == value2:
            return False
        self.roots[value2] = value1
        return True
