
def inp():
    return list(map(int, input().split()))

n = int(input())
p = set(inp()[1:])
q = set(inp()[1:])
print('I become the guy.' if len(p | q) == n else 'Oh, my keyboard!')

