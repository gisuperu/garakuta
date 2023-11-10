#H Cut And Multiplication
ra = int(input())
li = [int(s) for s in input().split()]
b = 0
c = 0
num =[0] * 2

for i in range(ra):
    if b > c:
        c += li[-(num[1] + 1)]
        num[1] += 1
    else:
        b += li[num[0]]
        num[0] += 1
# print(str(b) + ", " + str(c))
print(b * c)