import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from api import get_input

inp1 = get_input(
    part=1,
    day=10,
    year=2024,
)

# inp1 = \
# """**PCBS**
# **RLNW**
# BV....PT
# CR....HZ
# FL....JW
# SG....MN
# **FTZV**
# **GMJH**"""


grid = inp1.splitlines()

def extract_word(grid):
    n = len(grid)
    cols = [[] for _ in range(n)]
    rows = [[] for _ in range(n)]

    for j in (0, 1, n - 2, n - 1):
        for i in range(n):
            cols[i].append(grid[j][i])
            rows[i].append(grid[i][j])

    cols = cols[2:-2]
    rows = rows[2:-2]

    w = n - 4

    return "".join([(set(cols[i % w]) & set(rows[i // w])).pop()
                    for i in range(w*w)])

print("Part 1:", extract_word(grid))

# inp2 = get_input(
#     part=2,
#     day=10,
#     year=2024,
# )

inp2 = open("./inp2.txt").read() # use macros to convert grid of grids into single column

import string
def power(text):
    value = {j:i for i,j in enumerate(string.ascii_uppercase, 1) }
    return sum(i*value[j] for i,j in enumerate(text, 1))

grids = [ i.splitlines() for i in inp2.split('\n\n')]

print('Part 2:', sum( power(extract_word(g))  for g in grids  ))

