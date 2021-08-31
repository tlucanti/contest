from random import randint

with open('input.txt', 'w') as f:
    for i in range(100):
        s = randint(1, 10)
        s2 = ''.join(map(chr, [randint(65, 90) for j in range(s)]))
        r = randint(0, s)
        s1 = s2[:r] + chr(randint(65, 90)) + s2[r:]
        f.write(s1)
        f.write('\n')
        f.write(s2)
        f.write('\n')
