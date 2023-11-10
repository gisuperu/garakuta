#J Tree Color
from operator import mul
from functools import reduce

def main():
    li = [int(s) for s in input().split()]
    num = 0
    rem = li[3]
    rim = 1000000007

    def combine (n, r , s):
        numer = reduce(mul, range(n, n - r - s, -1), 1)
        denom1 = reduce(mul, range(1, r + 1), 1)
        denom2 = reduce(mul, range(1, s + 1), 1)
        return numer // (denom1 * denom2)

    for i in range((li[3] // li[1]) + 1):
        if i > li[0]:
            break
        elif rem % li[2] == 0:
            num += combine(li[0], i, (rem // li[2])) % rim
        rem -= li[1]
    
    print(num % rim)
if __name__ == '__main__':
    main()