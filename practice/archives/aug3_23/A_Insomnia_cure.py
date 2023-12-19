import sys
*A,d = map(int,sys.stdin.read().split())

print(sum(any((i%p==0) for p in A) for i in range(1,d+1)))


