
import itertools

a = list(itertools.chain(*[input() for _ in range(8)]))
w = a.count('Q') * 9 + a.count('R') * 5 + a.count('B') * 3 + a.count('N') * 3 + a.count('P')
b = a.count('q') * 9 + a.count('r') * 5 + a.count('b') * 3 + a.count('n') * 3 + a.count('p')
print('White' if w > b else ('Black' if b > w else 'Draw'))

