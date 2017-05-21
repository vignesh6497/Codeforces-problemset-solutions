#Codeforces Beta Round #85 (Div. 2 Only)
#Petya and Strings

str1 = input().lower()
str2 = input().lower()

for i in range(len(str1)):
    if str1[i] != str2[i]:
        if str1[i] < str2[i]:
            flag = 0
            break
        else:
            flag = 1
            break
    else:
        flag = 2
if flag == 0:
    print("-1")
elif flag == 1:
    print("1")
elif flag == 2:
    print("0")
