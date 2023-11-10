#C Palindrome Judgement
s = list(input())
for i in range(len(s) // 2):
    if s[i] != s[-(i+1)]:
        print("No")
        exit()
print("Yes")
