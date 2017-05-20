#Codeforces Round #173
#Bit++

n = int(input())
value = 0
for i in range(n):
    s = input()
    if s == '++X' or s == 'X++':
        value += 1
    elif s == '--X'or s == 'X--':
        value -= 1
print(value)
