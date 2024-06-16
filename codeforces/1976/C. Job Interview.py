import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    
    pc,tc = 0,0
    te, pr = [], []
    rnks = []
    for p,t in zip(A,B):
        if p > t:
            pr.append((p,t))
            pc += 1
            rnks.append(pc)
        else:
            te.append((p,t))
            tc += 1
            rnks.append(tc)
    # print('-----------------',file=sys.stderr)

    # print(*rnks, file=sys.stderr)
    # print(pr,file=sys.stderr)
    # print(te,file=sys.stderr)

    if len(pr) > n:
        # testing team consists of all tester appllicants and remaning programmers
        # and the programmming team just containst of first n programmers

        general_programming_strength = sum(i[0] for i in pr[:n]) 
        general_testing_strength = sum(i[1] for i in te) + sum(i[1] for i in pr[n:])
        
        gs = general_programming_strength + general_testing_strength
        # print(gs, file=sys.stderr)

        ans = []
        for i in range(n+m+1):
            # is candidate i among the first n programmers ?
            isdom = (A[i] > B[i]) and (rnks[i] <= n)
            # print(isdom, file=sys.stderr)
            if isdom:
                # then some problem occurs
                # the n+1th programmer gets accepted 
                ans.append(gs - pr[n][1] + pr[n][0] - A[i])
            else:
                # this guy was part of the testing team
                ans.append(gs - B[i])

    else:
        general_testing_strength = sum(i[1] for i in te[:m]) 
        general_programming_strength = sum(i[0] for i in pr) + sum(i[0] for i in te[m:])
        
        gs = general_programming_strength + general_testing_strength

        ans = []
        for i in range(n+m+1):
            # is candidate i among the first n programmers ?
            isdom = (A[i] < B[i]) and (rnks[i] <= m)
            if isdom:
                # then some problem occurs
                # the n+1th programmer gets accepted 
                ans.append(gs - te[m][0] + te[m][1] - B[i])
            else:
                # this guy was part of the testing team
                ans.append(gs - A[i])
    print(*ans)



    
    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# C. Job Interview
# 2000, 256
#
# https://codeforces.com/contest/1976/problem/C
# Thursday 30 May 2024 20:06:20 +0530
#
