
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input

inp1 =  get_input( part=1,
    day=1, 
    year=2024,
)



from collections import Counter

c = Counter(inp1)

print(f"Part1: {c['B'] +  c['C'] * 3}")


inp2 =  get_input( part=2,
    day=1, 
    year=2024,
)


pairs = [inp2[i:i+2] for i in range(0, len(inp2), 2)]

cost = dict(zip("xABCD",[0, 0,1,3,5]))

a2 = (sum(
    (cost[i] + cost[j] + 2*("x" not in i+j) ) for i,j in pairs
))

print(f"Part2: {a2}")

inp3 =  get_input( part=3,
    day=1, 
    year=2024,
)
triples = [inp3[i:i+3] for i in range(0, len(inp3), 3)]



s = 0

for t in triples:
    c = 3 - t.count("x")
    s += [0,0,2,6 ][c]
    s += sum(cost[i] for i in t)
    

print(f"Part3: {s}")
