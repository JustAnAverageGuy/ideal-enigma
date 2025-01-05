import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input

inp1 =  get_input( part=1,
    day=2, 
    year=2024,
)

runes, _, words = inp1.strip().strip('.').splitlines()
runes = runes.strip().split(':')[1].split(',')

s = 0
for r in runes:
    s += words.count(r)
print(f'Part 1: {s}')



inp2 =  get_input( part=2,
    day=2, 
    year=2024,
)


runes, _, *words = inp2.strip().strip('.').splitlines()
words_str = " ".join(words)
runes = runes.strip().split(':')[1].split(',')

runsym = set()

for i in range(len(words_str)):
    for r in runes:
        if words_str[i:].startswith(r) or words_str[i:].startswith(r[::-1]):
            for x in range(i, i+len(r)): runsym.add(x)


print(f'Part 2: {len( runsym )}')


inp3 =  get_input( part=3,
    day=2, 
    year=2024,
)


# inp3 = \
# """WORDS:THE,OWE,MES,ROD,RODEO
#
# HELWORLT
# ENIGWDXL
# TRODEOAL"""

runes, _, *words = inp3.strip().strip('.').splitlines()
runes = runes.strip().split(':')[1].split(',')

runes = [*runes, *(i[::-1] for i in runes)]

runsym = set()

H = len(words)
W = len(words[0])

for y in range(H):
    for x in range(W):
        for r in runes:
            # check horizontal
            cx = x
            cy = y
            cr = list(r)
            for rr in cr:
                if words[cy][cx] == rr:
                    cx += 1
                    cx %= W
                else:
                    break
            else:
                cx = x
                for _ in range(len(cr)):
                    runsym.add((y, cx))
                    cx += 1
                    cx %= W

            cx = x
            cy = y
            for rr in cr:
                if cy >= H: break
                if words[cy][cx] == rr:
                    cy += 1
                else:
                    break
            else:
                cy = y
                for r in range(len(cr)):
                    runsym.add((cy, x))
                    cy += 1
                    cx %= W


print(f'Part 3: {len( runsym )}')
