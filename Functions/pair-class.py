
class pair(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.__hash = hash((p1, p2))
    
    def __str__(self):
        return f'({self.p1}, {self.p2})'

    def __repr__(self):
        return self.__repr__()

    def __hash__(self):
        return self.__hash

