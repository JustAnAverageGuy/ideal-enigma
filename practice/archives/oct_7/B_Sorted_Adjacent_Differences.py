import sys;input=sys.stdin.readline
'''
⠄⠄⠄⠄⠄⠄⠄⢀⠤⣒⠍⣢⢗⡞⣿⣂⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢀⣴⠪⢕⢫⢚⣴⡏⣼⢋⣶⣮⠳⡆⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢠⡿⣵⢱⡇⢣⢟⣿⢜⣳⡿⠿⣿⡇⠿⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠸⣼⢣⢏⡴⠋⣺⣴⣷⠞⠛⢿⣿⠐⠂⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢸⢸⠄⡕⢄⢾⣿⣿⣿⣿⣿⣿⣛⣁⡇⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠈⣇⠃⡉⠉⠅⣿⣿⣿⣿⣿⣟⣍⣀⡃⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣟⠷⡅⢸⣿⣬⣛⡻⠿⣿⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢱⡭⠞⢻⣿⣿⣿⣿⣿⣿⠆⢰⡞⢝⡂⠄⠄⠄⠄⠄⠄
⠄⢀⣀⣤⣤⣶⢴⢃⣿⣿⣿⣿⡏⣿⠟⡄⣌⢷⣖⢭⣀⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⣿⡏⢸⢣⣾⣿⡹⣾⠋⣷⠹⡀⠙⡄⠄⠄
⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⡣⣿⣆⣗⠄⣿⡄⠄
⢸⣿⣿⣿⠿⡴⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢳⣌⢿⡘⢗⠻⢇⠄
⢸⣧⢩⣕⡔⡄⣿⣿⣿⣿⣷⠻⢫⣼⣿⣿⣿⣧⠘⡮⠓⣷⠠⡱⣤⠙
⠈⢣⡟⡌⠄⢳⢻⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢏⠦⣧⢣⡟⡀⢸⡉⠉
⠿⠸⢹⣤⠄⠄⠓⡝⢿⣿⣿⠇⣿⣿⣿⠟⡥⠊⣤⠄⠞⣼⣇⠤⠓⠄
⣫⡄⢆⢀⠄⠄⠄⠈⠢⡙⢫⣾⡜⢫⠕⠋⠄⠄⠄⢀⣾⣿⡇⠄⠄⠄
⣿⣿⠈⠣⣗⡀⡄⢆⢀⣨⣞⣥⣊⣀⣀⣀⣤⠴⠚⣿⣿⣿⡇⠄⠄⠄
⣿⣿⠄⠄⠄⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⡇⠄⠄⠄
'''
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().strip().split()))
    k = n//2
    d = -1
    sgn = -1
    A.sort()
    while 0<= k <= n-1:
        # print(k)
        print(A[k],end=' ')
        # print('d:', d)
        k += d
        d *= sgn 
        d += 1
        d *= -sgn
        
        sgn *= -1 
                
    print()
    