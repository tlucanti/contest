for t__ in range(int(input())):
    n = int(input())
    if n != 3:
        s1 = input()
        s2 = input()
        for i in range(n - 4):
            s__ = input()
        s3 = input()
        s4 = input()
        s1 = int(s1[1])
        s2 = int(s2[0])
        s3 = int(s3[-1])
        s4 = int(s4[-2])
    else:
        s1 = input()
        s2 = input()
        s3 = input()
        s1 = int(s1[1])
        s2_ = int(s2[0])
        s3_ = int(s2[-1])
        s4 = int(s3[-2])
        s2 = s2_
        s3 = s3_
    if s1 == s2 == s3 == s4:
        print(2)
        print(1, 2)
        print(2, 1)
    elif s1 == s2 and s3 == s4:
        print(0)
    elif s1 == s2 and s3 != s4:
        print(1)
        if s3 == s1:
            print(n - 1, n)
        else:
            print(n, n - 1)
    elif s3 == s4 and s1 != s2:
        print(1)
        if s1 == s3:
            print(1, 2)
        else:
            print(2, 1)
    elif s1 == s3 and s2 == s4:
        print(2)
        print(2, 1)
        print(n - 1, n)
    else:
        print(2)
        print(2, 1)
        print(n, n - 1)
