
# import sys
mask = [pow(41,i) for i in range(10)]
# assert mask[-1] <= 2 * (10 ** 16)
def solve():
    n = int(input())
    print(*mask[:n],flush=True)
    # print("idhar aa gya",flush=True,file=sys.stderr)
    k = int(input())
    A = []
    while k > 0:
        A.append(k% 41)
        k //= 41
    print(*A,flush=True)
    
    

for _ in range(int(input())): solve()