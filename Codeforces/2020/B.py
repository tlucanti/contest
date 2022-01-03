
for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    st = set()
    for i in range(len(s)):
        if s[i] not in st:
            st.update({s[i]})
        else:
            st.update({s[i] + 1})

    print(len(st))
