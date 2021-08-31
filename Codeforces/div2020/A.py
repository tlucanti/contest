
for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    st = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            st.update({s[j] - s[i]})
    print(len(st))
