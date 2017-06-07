# Codeforces Beta Round #87
# Tram

n = int(input())
temp = 0
ans = 0
for i in range(n):
    leave, enter = map(int,input().split())
    temp = temp - leave
    temp = temp + enter
    if temp > ans:
        ans = temp
print(ans)
