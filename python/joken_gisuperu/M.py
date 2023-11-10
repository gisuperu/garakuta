#M Huge Amount Of Computation
def main():
    ra = [int(s) for s in input().split()]
    ali = [int(s) for s in input().split()]
    bli = [int(s) for s in input().split()]
    res = 0
    rim = 1000000007

    for i in range(ra[0]):
        for j in range(i, ra[0]):
            for k in range(ra[1]):
                for l in range(k, ra[1]):
                    res += (ali[j] - ali[i]) * (bli[l] - bli[k])
                res %= rim
            res %= rim
        res %= rim
    print(res)



if __name__ == '__main__':
    main()
