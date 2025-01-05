import os
import sys


sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input



inp1 =  get_input( part=3,
    day=3, 
    year=2024,
)

# inp1 = \
# """..........
# ..###.##..
# ...####...
# ..######..
# ..######..
# ...####...
# .........."""





padding_len = 3
A = [ [int(j == '#') for j in i.strip()]    for i in inp1.splitlines()]

for i in range(padding_len): A.insert(0, [0]*len(A[0]))
for i in range(padding_len): A.append([0]*len(A[0]))
for j in A:
    for _ in range(padding_len): j.append(0)
    for _ in range(padding_len): j.insert(0,0)

B = [list(i) for i in A]

from time import sleep
def show(arr):
    print("\033[3H",end="")
    colors = "⬜⬛🟥🟦🟧🟨🟩🟪🟫" 
    for i in arr: print(*[colors[j % len(colors)] for j in i], sep="",flush=True); sleep(0.05)
    sleep(0.25)
    print('-'*len(arr[0]))

H = len(A)
W = len(A[0])

def update(c):
    global A
    global B
    any_change = False
    for i in range(1,H-1):
        for j in range(1,W-1):
            if A[i-1][j] == A[i][j-1] == A[i+1][j] == A[i][j+1] == A[i-1][j-1] == A[i-1][j+1] == A[i+1][j-1] == A[i+1][j+1] == A[i][j] == c:
                B[i][j] = c+1
                any_change = True
    A = [list(i) for i in B]
    return any_change



i = 1
show(B)
while update(i):
    show(B)
    i += 1

print(sum(sum(i) for i in A))
