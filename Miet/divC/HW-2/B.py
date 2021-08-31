print(["NO", "YES"][(lambda n, k: (int(n) // int(k)) % 2)(*input().split())])
