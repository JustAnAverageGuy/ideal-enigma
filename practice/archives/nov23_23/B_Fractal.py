import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')
n,k = map(int,input().strip().split())
A = [input().strip() for i in range(n)]
# A = [input().strip().replace(".","⬜").replace('*',"⬛") for i in range(n)]

WHITE = '.'
BLACK = '*'

for y in range(n**k):
    for x in range(n**k):
        ty = y
        tx = x
        for generations in range(k):
            cury, curx = ty%n, tx%n
            ty //= n
            tx //= n
            if A[cury][curx] == BLACK:
                print(BLACK, end='')
                break
        else:
            print(WHITE,end='')
    print('')