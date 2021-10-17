 # import time

def quicksort(lst):
    _l = len(lst)
    req_sort_q(lst, 0, _l)


def req_sort_q(lst, start, end):
    _l, r = start, end
    _k = lst[(_l + r) // 2]
    l_ = 0
    r_ = 0
    while _l < r:
        if l_ == 0 and lst[_l] < _k:
            _l += 1
        else:
            l_ = 1
        if r_ == 0 and lst[r] >= _k:
            r += 1
        else:
            r_ = 1
        if l_ and r_:
            lst[_l], lst[r] = lst[r], lst[_l]
            l_, r_ = 0, 0
    lst[k], lst[r] = lst[r], lst[k]
    req_sort_q(lst, start, r - 1)
    req_sort_q(lst, r, end)


def array_index(arr, i):
    __i = 0
    cur = 0
    while __i < x:
        cur = arr.get(__i, -1)
        if cur != -1:
            i -= 1
        if i < 0:
            break
        __i += 1
    return cur


def array_rindex(arr):
    __i = x - 1
    while __i >= 0:
        cur = arr.get(__i, -1)
        if cur != -1:
            return cur
        __i -= 1


def create_array():
    global clocks

    _array = {}
    times = input().split()
    # global t_1
    # t_1 = time.time()
    __i = 0
    while __i < n:
        ti = int(times[__i])
        if _array.get(ti % x, -1) == -1:
            clocks += 1
            _array[ti % x] = ti
        elif _array[ti % x] > ti:
            _array[ti % x] = ti
        __i += 1

    # i = 0
    # _l = len(_array)
    # while i < _l:
    #     if _array[i] == -1:
    #         _array.pop(i)
    #         _l -= 1
    #         i -= 1
    #     i += 1
    times.clear()
    return _array


n, x, k = input().split()
n, x, k = int(n), int(x), int(k)

clocks = 0
array = create_array()
s = (k - 1) % clocks
clock_array = sorted(array.values())

# for i in range(x):
#     if clock_array[i] != -1:
#         clock_array = clock_array[i:]
#         break

# array.append(array_index(array, 0))
activated_clocks = 0
total_clocks = 0
loops = 0
# print(t2 := time.time() - t_1)

f = 1
if k == 1:
    print(clock_array[0])
    f = 0

while f:
    total_clocks

    while activated_clocks < clocks and clock_array[activated_clocks] < loops * x:
        activated_clocks += 1

    if total_clocks == k:
        if activated_clocks < clocks:
            array.clear()
            del array
            clock_array = clock_array[:activated_clocks]
            clock_array.sort(key=lambda __n: __n % x)
            last_clock = clock_array[-1]
        else:
            last_clock = array_rindex(array)
        extra_loops = last_clock // x
        # print("=", last_clock)
        print(last_clock + (loops - extra_loops - 2) * x)
        break
    if total_clocks + activated_clocks > k:
        if activated_clocks < clocks:
            array.clear()
            del array
            clock_array = clock_array[:activated_clocks]
            clock_array.sort(key=lambda __n: __n % x)
            last_clock = clock_array[k - total_clocks - 1]
        else:
            last_clock = array_index(array, k - total_clocks - 1)
        extra_loops = last_clock // x
        # print(">", last_clock)
        print(last_clock + (loops - extra_loops - 1) * x)
        break

    if activated_clocks < clocks:
        add_clocks = activated_clocks * (clock_array[activated_clocks] // x - loops + 1)
        if total_clocks + add_clocks <= k:
            total_clocks += add_clocks
            loops = clock_array[activated_clocks] // x + 1
        else:
            loops += (k - total_clocks) // activated_clocks
            total_clocks += ((k - total_clocks) // activated_clocks) * (activated_clocks)

    else:
        loops += (k - total_clocks) // clocks
        total_clocks += ((k - total_clocks) // clocks) * (clocks)

# print(t3 := time.time() - t2)
