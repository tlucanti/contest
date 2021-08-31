
def pal_check(s):
    if s[0:len(s) // 2] == s[:len(s) // 2 - (len(s) + 1) % 2:-1]:
        return 1
    return 0


st = input()
if pal_check(st):
    print(0)
else:
    print(4)
    print('R', len(st) - 1)
    print('L', 2)
    print('R', 2)
    print('R', 2 * len(st) + 1)
