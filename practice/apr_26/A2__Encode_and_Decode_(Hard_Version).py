s = input().strip()

b25 = [chr(ord('a')+i) for i in range(25)]
bb25 = {j:i for i,j in enumerate(b25)} # fuck good variable names

# max( log(ai) * n ) = log(1e9)*1e4 < 65k < 1e5 

def encode_b25(A):
    res = []
    for n in A:
        hm = []
        while n:
            hm.append(b25[n%25])
            n //= 25
        res.append("".join(hm[::-1]))

    return 'z'.join(res)



def decode_b25(s):
    res = s.split('z')
    A = []
    for w in res:
        a = 0
        for c in w:
            a *= 25
            a += bb25[c]
        A.append(a)
    return A



if s == "first":
    n = int(input())
    A = list(map(int,input().strip().split()))
    print(
        encode_b25(A)
    )
else:
    assert s == 'second'
    s = input().strip()
    A = decode_b25(s)
    print(len(A))
    print(*A)


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# A2. Encode and Decode (Hard Version)
# 2000, 512
#
# https://codeforces.com/contest/2168/problem/A2
# Monday 13 April 2026 16:43:26 +0530
#
# vim:fdm=marker:
