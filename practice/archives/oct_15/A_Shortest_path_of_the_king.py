from collections import deque


board = [[None]*8 for i in range(8)]
path = [[None]*8 for i in range(8)]

source = input()
dest = input()

dirn = [(i,j) for i in range(-1,2) for j in range(-1,2) if i or j]

ro  = int(source[1])-1
col = ord(source[0])-ord('a')

qu = deque([(ro,col,0,0)])

tro  = int(dest[1])-1
tcol = ord(dest[0])-ord('a')


while qu:
    r,c,dr,dc = qu.popleft()
    
    if board[r][c] is None:
        if board[r-dr][c-dc] is None:
            board[r][c] = 0
        else:
            board[r][c] = board[r-dr][c-dc] + 1
        path[r][c] = 'L'*(dc<0)+'R'*(dc>0)+'D'*(dr<0)+'U'*(dr>0)
    
        for dr,dc in dirn:
            if 0<=r+dr<=7 and 0<=c+dc<=7:
                qu.append((r+dr,c+dc,dr,dc))

print(board[tro][tcol])

r = tro
c = tcol

finalpath = list()

while r!=ro or c!=col:
    di = path[r][c]
    finalpath.append(di)
    c += ('L' in di) - ('R' in di)
    r += ('D' in di) - ('U' in di)


print(*finalpath[::-1],sep='\n')
                