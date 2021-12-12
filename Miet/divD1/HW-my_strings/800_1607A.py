

##
#	Author:		antikostya
#	Created:	2021-11-02 17:33:04
#	Modified:	2021-11-02 17:38:39
##
 
for _t in range(int(input())):
    a = input()
    s = input()
    c = a.index(s[0])
    ans = 0
    for i in s[1:]:
    	ans += abs(c - a.index(i))
    	c = a.index(i)
    print(ans)
 
