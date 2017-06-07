#Codeforces round #163
#Stones on the table

n = int(input())
seq = input()
count = 0
for i in range(n-1):
    if seq[i] == seq[i+1]:
        count += 1
print(count)
