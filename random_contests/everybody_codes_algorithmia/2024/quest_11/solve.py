import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input

# inp =  get_input( part=3,
#     day=11, 
#     year=2024,
# )
# with open("in3","w") as f: f.write(inp)

with open("in3") as f: inp = f.read()

# inp = \
# """A:B,C
# B:C,A
# C:A"""


evolutions = {}

for i in inp.splitlines(keepends=False):
    a,b = i.split(':')
    bl = b.split(',')
    evolutions[a] = bl


enc = {j:i for i,j in enumerate(evolutions)}


simpevo = {
    enc[i]:[enc[k] for k in j] for i,j in evolutions.items()
}

def give_next_generation(simpevo, cur):
    nex = [0]*len(simpevo)
    for i,j in simpevo.items():
        for k in j: nex[k] += cur[i]
    return nex

def check(X):
    init = [0]*len(enc)


    init[enc[X]] = 1


    for _ in range(20):
        init = [i for i in give_next_generation(simpevo, init)]

    # print(init)
    # print(sum(init))
    return sum(init)

hmm = []

for i in enc:
    hmm.append(check(i))

print(max(hmm) - min(hmm))


