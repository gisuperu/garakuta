#B Need Water
yen = int(input())
val = [int(s) for s in input().split()]
wat = 0

wata = (yen // val[1]) * val[0]
watb = (yen // val[3]) * val[2]
if(wata > watb):
    print(wata)
else:
    print(watb)