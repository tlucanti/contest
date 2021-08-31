
nums = set(input().split())
print('\n'.join(["Lucky" if len(set(input().split()) & nums) >= 3 else "Unlucky" for i in range(int(input()))]))
