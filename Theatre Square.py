#Codeforces Beta Round #1
#Theatre Square
import math
n, m, a = map(int, input().split())
n = math.ceil(n/a)
m = math.ceil(m/a)
print (int(n*m))
