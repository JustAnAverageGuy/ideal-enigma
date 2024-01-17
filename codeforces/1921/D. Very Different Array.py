import sys;input=sys.stdin.readline

def solve():
    n,m = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    
    la = 0
    ra = n - 1
        
    l = 0
    r = m - 1

    d = 0

    A.sort()
    B.sort()
    cnt = 0;
    while(cnt != n):
        d1 = abs(A[la] - B[l]);
        d2 = abs(A[la] - B[r]);
        d3 = abs(A[ra] - B[l]);
        d4 = abs(A[ra] - B[r]);
        mx1 = max(d1,d2); mx2 = max(d3,d4);
        mx = max(mx1,mx2);
        d+=mx;
        if(mx1 >= mx2):
            la += 1
            if(d1 >= d2):
                l+=1;
            else:
                r-=1;
        else:
            ra-=1;
            if(d3>=d4):
                l+=1;
            else:
                r-=1;
        cnt+= 1;
    print(d)


    

for _ in range(int(input())): solve()




















# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# D. Very Different Array
# 2000, 256
#
# https://codeforces.com/contest/1921/problem/D
# Monday 15 January 2024 20:11:30 +0530
#
