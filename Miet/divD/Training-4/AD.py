
s = input()
if len(s) == 1:
    print(s.swapcase())
else:
    if s[1:].isupper():
        print(s.swapcase())
    else:
        print(s)
