import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input

inp1 =  get_input( part=1,
    day=4, 
    year=2024,
)


inp1 =  get_input( part=3,
    day=4, 
    year=2024,
)



hs = [int(i) for i in inp1.strip().split()]

hs.sort()

n = len(hs)
if n%2 == 1:
    median1 = median2 = hs[n // 2]
else:
    median1 = hs[n//2]
    median2 = hs[n//2 + 1]



print(min(sum(abs(i - median1) for i in hs), sum(abs(i-median2) for i in hs) ))

