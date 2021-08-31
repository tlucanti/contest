
for t__ in range(int(input())):
    s = 0
    x = input()
    s += (int(x[0]) - 1) * 10
    for i in range(len(x)):
        s += i + 1
    print(s)
