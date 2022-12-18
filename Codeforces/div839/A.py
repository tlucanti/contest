
def inp():
    return list(map(int, input().split()))

for _ in range(int(input())):
    a = input()
    exec(f'print({a})')


