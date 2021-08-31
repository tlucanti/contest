
class list(list):

    def __init__(self, seq=()):
        super().__init__(seq)

    def pr(self):
        print(self)

    def __rshift__(self, other):
        self.append(self[0])
        self.pop(0)
        return self


lst = list('1')
lst.append('2')
lst.pr()
lst >> 1
lst.pr()
