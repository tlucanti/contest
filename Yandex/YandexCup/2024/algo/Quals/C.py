
def solve(s, ex):
    pos = 0
    min_pos = 0
    max_pos = 0

    for c in s:
        if c == 'L':
            pos += 1
        elif c == 'R':
            pos -= 1
        else:
            max_r = max(max_pos, pos + 1)
            min_r = min(min_pos, pos)

            max_l = max(max_pos, pos)
            min_l = min(min_pos, pos - 1)

            if ex:
                expr = (max_r - min_r >= max_l - min_l)
            else:
                expr = (max_r - min_r > max_l - min_l)

            if expr:
                pos += 1
                max_pos = max_r
                min_pos = min_r
            else:
                pos -= 1
                max_pos = max_l
                min_pos = min_l

        max_pos = max(max_pos, pos)
        min_pos = min(min_pos, pos)
    return max_pos - min_pos

s = input()
print(max(solve(s, 0), solve(s, 1)))

