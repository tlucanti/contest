
class list(list):
    def __init__(self, seq=()):
        super().__init__(seq)

    def __rshift__(self, other):
        for __i in range(other):
            self.insert(0, self[-1])
            self.pop()
            return self
        for __i in range(-other):
            self.append(self[0])
            self.pop(0)
            return self

    def pr(self, sep=' '):
        print(sep.join(map(str, self)))


n = input()
a = list(input().split()) >> 1
a.pr()
