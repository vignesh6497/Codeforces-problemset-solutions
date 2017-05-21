#Codeforces Round #143 (Div. 2)
#Team

n = int(input())
temp = 0
for i in range(n):
    count = 0
    p, v, t = map(int,input().split())
    if p==1:
        count +=1
    if v==1:
        count +=1
    if t==1:
        count +=1
    if count>1:
        temp +=1
print(temp)
        
        
