print(' '.join(map(str, list(filter(lambda x: ~x % 2, map(int, input().split()))))))
