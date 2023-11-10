import itertools

def print_iplist(iplist):
    for key in iplist.keys():
        print("{0:08b} {1:08b}".format(int(key), iplist[key]))


def different(ip1, wildcard1, ip2, wildcard2):
    diff = ip1 ^ ip2 # ipの差分を抽出
    wildcard = wildcard1 | wildcard2 # wildcardを統合

    diff = diff & ~wildcard # wildcard以外のip差分をさらに抽出

    # 1のビットが1つ以下か判定(なければ0をreturn)
    bitmask = 1
    while(diff & bitmask == 0 and bitmask < 256):
        bitmask <<= 1
    if diff != bitmask:
        return 0
    
    # 差が一つしかないことが確認できたため新しいwildcardをreturn
    return wildcard | diff



def reduce(iplist):
    # 統合出来るものがなくなるまで続ける
    next_iplist = dict()
    for i in range(len(iplist)):
        for key_pair in itertools.combinations(iplist.keys(), 2):
            ip1 = [int(key_pair[0]), iplist[key_pair[0]]]
            ip2 = [int(key_pair[1]), iplist[key_pair[1]]]

            # ipアドレス同士(ワイルドカード込み)の差分が1箇所以内なら減らす
            new_wildcard =  different(ip1[0], ip1[1], ip2[0], ip2[1])
            if new_wildcard != 0:
                next_iplist[ip1[0] & ~new_wildcard] = new_wildcard
            else:
                if ip1[0] not in next_iplist.keys():
                    next_iplist[ip1[0]] = ip1[1]
                if ip2[0] not in next_iplist.keys():
                    next_iplist[ip2[0]] = ip2[1]
        print_iplist(next_iplist)
        print()
        iplist = next_iplist
    
    return next_iplist

def main():
    begin = 0;
    end = 16;

    iplist = dict()
    # 許可したいIPアドレス一覧作成
    for i in range(begin, end+1, 1):
        iplist[i] = 0;

    # IPアドレスの統合
    iplist = reduce(iplist)

    # 出力
    print_iplist(iplist)

def test():
    print("{0:08b}".format(different(15, 4, 3, 0)))

if  __name__ == "__main__":
    main()
    #test()
