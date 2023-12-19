# import sys;input=sys.stdin.readline

# def solve():
    # n = int(input())

                
    
        

for _ in range(int(input())):
    A = [input() for i in range(10)]
    # print(A)
    score = 0
    for x in range(10):
        for y in range(10):
            # print((x,y))
            if A[y][x] == 'X':
                # print((x,y),end=' ')
                X,Y = x,y
                if Y > 4: Y = 9 - Y
                if X > 4: X = 9 - X
                # B.append((Y,X))
                points = min(X,Y) + 1
                score += points
                # print(points)
                
    print(score)