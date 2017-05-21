#Codeforces Round #197 (Div. 2)
#Helpful Maths

str1 = input()
a = str1.count('1')
b = str1.count('2')
c = str1.count('3')
d = str1.count('+')

for i in range(a):
    print("1",end="")
    if d>0:
        print("+",end="")
        d -=1
for j in range(b):
    print("2",end="")
    if d>0:
        print("+",end="")
        d -=1
for k in range(c):
    print("3",end="")
    if d>0:
        print("+",end="")
        d -=1
