#Codeforces Beta Round #89
#String Task

inp = input()
temp = ""
for i in range(len(inp)):
    if inp[i] == "y" or inp[i] == "Y" or inp[i] == "a" or inp[i] == "e" or inp[i] == "i" or inp[i] == "o" or inp[i] == "u" or inp[i] == "A" or inp[i] == "E" or inp[i] == "I" or inp[i] == "O" or inp[i] == "U":
        continue
    else:
        temp = temp+"."+inp[i].lower()
print(temp)
