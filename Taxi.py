#VK Cup 2012 Qualification Round 1
#Taxi

import math
n = int(input())
grp = [int(x) for x in input().split()]
total = 0
a = grp.count(1)
b = grp.count(2)
c = grp.count(3)
d = grp.count(4)

total = d+c+int(b/2)

a -= c

if b%2 == 1:
    total += 1
    a -= 2
if a>0:
    total += int((a+3)/4)
print(int(total))


