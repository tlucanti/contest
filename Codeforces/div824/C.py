#
# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     d = [-1] * 26
#     z = [-1] * 26
#     nx = 0
#     if s[0] == 'a':
#         nx += 1
#     for i in s:
#         o = ord(i) - ord('a')
#         if d[o] == -1:
#             if o in d and o == 0:
#                 nx = (nx + 1) % 26
#             d[o] = nx
#             nx = (nx + 1) % 26
#     for i in s:
#         o = ord(i) - ord('a')
#         c = d[o]
#         print(chr(c + ord('a')), end='')
#     print()

def check_loop(f):
    q = 1
    ff = f
    f = d[f]
    while True:
        if f == ff:
            return q
        if f == -1:
            return 26
        f = d[f]
        q += 1


for _ in range(int(input())):
    n = int(input())
    s = input()
    d = [-1] * 26
    z = [-1] * 26
    for i in s:
        o = ord(i) - ord('a')
        if d[o] == -1:
            nx = 0
            while True:
                if nx in d:
                    nx = (nx + 1) % 26
                    continue
                d[o] = nx
                if o == nx or check_loop(nx) < 26:
                    nx = (nx + 1) % 26
                    continue
                break
    for i in s:
        o = ord(i) - ord('a')
        c = d[o]
        print(chr(c + ord('a')), end='')
    print()

