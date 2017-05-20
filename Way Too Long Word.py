#Codeforces Beta Rounnd #65
#Way Too Long Words

n = int(input())
for i in range(n):
    ip_word = input()
    length = len(ip_word)
    if(length>10):
        print(ip_word[0]+str(length-2)+ip_word[length-1])
    else:
        print(ip_word)
        
