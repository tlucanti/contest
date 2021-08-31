
for t__ in range(int(input())):
    a = input()
    # lst = []
    size = 0
    # last = ''
    for i in a:
        # if len(lst) == 0 or i == 'a':
        #     lst.append(i)
        # elif lst[-1] ==
        #
        size += 1
        if size >= 2 and i == 'B':
            size -= 2
    # if size > 1 and a[-1] == 'B':
    #     size -= 2
    print(size)
