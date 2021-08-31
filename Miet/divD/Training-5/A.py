
inp = open('input.txt', 'r')
d = {}
all = True
n = int(inp.readline().strip())
for i in range(n):
    s = hash(inp.readline().strip())
    d[s] = d.get(s, 0) + 1

inp.seek(0)
out = open('output.txt', 'w')
for i in range(n + 1):
    s = inp.readline().strip()
    h = hash(s)
    if d.get(h, 0) % 2:
        out.write(s + '\n')
        del d[h]
        all = False
if all:
    out.write('FAIL\n')
out.close()
inp.close()
