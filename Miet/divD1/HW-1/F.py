# -*- coding: utf-8 -*-
# @Author: kostya
# @Date:   2021-11-13 16:37:42
# @Last Modified by:   kostya
# @Last Modified time: 2021-11-13 16:47:52

array = list(range(8001))

def next_dis(n):
    n += 1
    while len(set(str(n))) != 4:
        n += 1
    return n

for i in range(1000, 9001):
    array[i - 1000] = next_dis(i)

# print(array)

import textwrap

a = str(array)[1:-1]
w = textwrap.wrap(a, 72)
print(w)
