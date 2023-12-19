def solve():
    A = [input() for i in range(8)]
    At = "".join([A[k%8][k//8] for k in range(64)]).strip(".")
    print(At)

for _ in range(int(input())):
    solve()