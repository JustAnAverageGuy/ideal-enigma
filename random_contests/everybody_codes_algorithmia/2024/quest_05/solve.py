import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input

inp =  get_input( part=3,
    day=5, 
    year=2024,
)

# inp = \
# """2 3 4 5
# 3 4 5 2
# 4 5 2 3
# 5 2 3 4"""

# inp = \
# """2 3 4 5
# 6 7 8 9"""

A = [[int(j) for j in i.split()] for i in inp.splitlines(keepends=False)]
# print(*A,sep='\n')
B = [ [i[j] for i in A] for j in range(len(A[0]))  ]


print(len(B[0]))
def dance(grid:list[list[int]], cur_col):

    # grid is transposed, so that columns are rows

    i = cur_col % len(grid)
    top = grid[i].pop(0)
    nx = grid[(i+1)%len(grid)]
    n = len(nx)
    idx = (top - 1) % (2 * n) # -1 to account for 1 based indexing
    if idx  < n:
        nx.insert(idx, top)
    else:
        idx = 2 * n - idx
        nx.insert(idx, top)

    return 

from collections import defaultdict

hmm = defaultdict(int)
seen = set()
for rounds in range(1,1000000000):
    dance(B, rounds-1)
    redcol = "".join(str(i[0]) for i in B)
    # hmm[redcol] += 1
    seen.add(int(redcol))
    # print(f'{rounds:4}->{redcol}->{hmm[redcol]}')
    # if hmm[redcol] == 2024:
    #     print(rounds)
    #     print(redcol)
    #     print(rounds * int(redcol))
    #     break
    # print(f'round: {rounds + 0:2}: {redcol} -> {hmm[redcol]}')
    if rounds % 1000000 == 0:
        print(max(seen))
print("Max size: ",max(hmm.values()))

# Plain bruteforce works, so not going to analyze this much more
