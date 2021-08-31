
print(['=', '>', '<'][(lambda x: 0 if x == 0 else (1 if x > 0 else -1))(int(input()) - int(input()))])
