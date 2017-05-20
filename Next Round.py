#VK Cup 2012 Qualification Round 1
#Next Round

n, k = map(int,input().split())
score = []
score = list(map(int,input().split()))
c = 0
score.sort(reverse=True)
for i in range(n):    
    if score[i]>= score[k-1]:
        if score[i]!= 0:
            c = c+1
print(c)
