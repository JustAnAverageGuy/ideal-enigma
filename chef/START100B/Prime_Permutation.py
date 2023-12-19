def get_primes(n):
  m = n+1
  #numbers = [True for i in range(m)]
  numbers = [True] * m #EDIT: faster
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

pri = get_primes(100000)

import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    if n == 2:
        print(-1)
        return
    for p in pri:
        if p > n:
            print(-1)
            return
        if n - p in pri:
            print(*range(n - p+1, n+1),*range(1,n - p + 1))
            return
    

for _ in range(int(input())): solve()

                