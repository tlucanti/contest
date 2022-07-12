
def inp():
    return list(map(int, input().split()))


class State:
    def __init__(self, penalty, div):
        self.penalty = penalty
        self.div = div

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'{self.penalty}({self.div})'


def arr_div(a):
    return [x // 2 for x in a]


def cumsum(a):
    n = len(a)
    out = [0] * n
    out[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        out[i] = a[i] + out[i + 1]
    return out


for _ in range(int(input())):
    n, k = inp()
    a = inp()
    divs = [a]
    for i in range(31):
        divs.append(arr_div(divs[-1]))
    cms = []
    for i in range(len(divs)):
        cms.append(cumsum(divs[i]))
    penalties = []
    for i in range(len(divs) - 1):
        penalties.append([x - y for x, y in zip(cms[i], cms[i + 1])])
    pay = [0] * n
    free = [0] * n
    pay[0] = State(k, 0)
    free[0] = State(penalties[0][0], 1)
    full_buy = []
    sm = 0
    for i in range(n):
        _s = 0
        for j in range(31):
            if i + j >= n:
                break
            _s += a[i + j] // 2 ** (j + 1)
        full_buy.append(sm + _s)
        sm += a[i] - k
    for i in range(1, n):
        if pay[i - 1].penalty < free[i - 1].penalty:
            state = pay[i - 1]
        else:
            state = free[i - 1]
        pay[i] = State(state.penalty + k, state.div)
        if state.div > 30:
            pen_i = 0
        else:
            pen_i = penalties[state.div][i]
        free[i] = State(state.penalty + pen_i, state.div + 1)
    # print(pay)
    # print(free)
    # print(full_buy)
    full_buy = max(full_buy)
    print(max(sum(a) - min(pay[-1].penalty, free[-1].penalty), full_buy))
