# import os
# import sys
#
# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
# )
#
# from api import get_input
#
# inp1 =  get_input( part=2,
#     day=7, 
#     year=2024,
# )

# inp1=\
# """A:+,-,=,=
# B:+,=,-,+
# C:=,-,+,+
# D:=,=,=,+"""

inp1 = open("inp").read()

from itertools import cycle

a = {}
for i in inp1.splitlines():
    x, y = i.strip().split(':')
    y = y.split(',')
    a[x] = y

def get_sum(patt, track, n):
    ini = 10
    tot = 0
    cnt = 0
    if DEBUG:
        print()
    for x,t in zip(cycle(patt), cycle(track)):
        if cnt > n: return tot
        if t == '+': ini += 1
        elif t == '-': ini = max(0, ini-1)
        else:
            if t == 'S': cnt += 1
            if x == '+': ini += 1
            elif x == '-': ini = max(0, ini-1)
        if DEBUG: print(f'{t}{x}{ini}',end=' ')
        tot += ini
    assert False



trackraw = \
"""S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""

trackraw = \
"""S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=       
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =          
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-"""

tracklines = [i for i in trackraw.splitlines(keepends=False)]
track = ["S"]
dirn = (1, 0)
x = 1
y = 0
WIDTH = len(tracklines[0])
HEIGHT = len(tracklines)



def isbad(nx,ny):
    return (not ((0 <= nx < WIDTH) and (0 <= ny < HEIGHT))) or (tracklines[ny][nx] == ' ')

import time
while True:

    # if not ((0<= x < WIDTH) and (0 <= y < HEIGHT))

    if tracklines[y][x] == 'S': break

    track.append(tracklines[y][x])

    # print(x,y, dirn,track,flush=True)
    # time.sleep(0.5)
    
    
    nx, ny = x + dirn[0], y + dirn[1]
    if not isbad(nx, ny):
        x = nx
        y = ny
    else:
        for d in [(0,1),(1,0),(-1,0),(0,-1)]:
            if d[0] == -dirn[0] or d[1] == -dirn[1]: continue 
            nx = x + d[0]
            ny = y + d[1]
            if not isbad(nx, ny):
                x = nx
                y = ny
                dirn = d
                break
        else:
            assert False

print('Track:\n',*track, sep="")


# trackraw = \
# """S+===
# -   +
# =+=-+"""



# tracklines = [i.strip() for i in trackraw.splitlines()]
# track = tracklines[0][1:]
# for j in tracklines[1: -1]: track += j[-1]
# track += tracklines[-1][::-1]
# for j in tracklines[len(tracklines)-2: 0:-1]: track += j[0]
# track += trackraw[0]


DEBUG = True
DEBUG = False
# for i,j in a.items(): print(i, get_sum(a[i], track, 1-1))


DEBUG = False
# print(*sorted(a, key=lambda x: get_sum(a[x],track, 10-1), reverse=True), sep="")

strategies = []
from itertools import combinations

for c in combinations(range(11), 5):
    cc = list(c)
    untaken = set(range(11)) - set(cc)
    for d in combinations(untaken, 3):
        hmm = ['=']*11
        for i in cc: hmm[i] = '+'
        for i in d: hmm[i] = '-'
        strategies.append([*hmm])
print(len(strategies), flush=True)


c = 0
opponent = a['A']
opp_score = get_sum(opponent, track, 2024 - 1)

from tqdm import tqdm

for strat in tqdm(strategies):
    my = get_sum(strat, track, 2024 - 1)
    if my > opp_score:
        c += 1

print(c)

    
