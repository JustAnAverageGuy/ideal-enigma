import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    A = list(map(int,input().strip().split()))
    # compute prefix mex of something and then find i such that mex(A[:i]) == mex(A[i:])
    # then you are done 
    seen = [0]*(n)
    mex_prefix = [int(A[0]==0)]
    seen[A[0]] = 1
    for i in range(1,n):
        if A[i] == mex_prefix[-1]:
            # find new mex
            for k in range(mex_prefix[-1]+1, n):
                if not seen[k]:
                    break
            else:
                print(-1)
                return
            mex_prefix.append(k)
        else:
            mex_prefix.append(mex_prefix[-1])
        seen[A[i]] = 1
    seen = [0]*n

    seen[A[-1]] = 1
    mex_suffix = [int(A[-1] == 0)]

    # print(mex_prefix,file=sys.stderr)
    
    if mex_suffix[-1] == mex_prefix[-2]:
        print("2")
        print(f'1 {n-1}')
        print(f'{n} {n}')
        return
    for i in range(n-2,-1,-1):
        # do same thing
        
        if A[i] == mex_suffix[-1]:
            # find new mex
            for k in range(mex_suffix[-1]+1, n):
                if not seen[k]:
                    break
            else:
                print(-1)
                return
            mex_suffix.append(k)
        else:
            mex_suffix.append(mex_suffix[-1])
    
        # print('suf',mex_suffix,file=sys.stderr)
        
        if (n>i-1>=0) and mex_suffix[-1] == mex_prefix[i-1]:
            print("2")
            print(f'1 {i}')
            print(f'{i+1} {n}')
            return
            

        seen[A[i]] = 1
    print(-1)

        



for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# B. Informatics in MAC
# 1000, 256
#
# https://codeforces.com/contest/1935/problem/B
# Tuesday 05 March 2024 20:06:55 +0530
#
