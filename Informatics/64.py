
n = input()
s = input().split()
print(' '.join([i for i in s if (int(i) + 1) % 2]))
