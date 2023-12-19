import sys;input=sys.stdin.readline


def indices_to_be_removed_nex(s):
    indices = []
    A = [0]
    i = 1
    n = len(s)
    while i < n:
        if ord(s[A[-1]]) > ord(s[i]):
            while A and (ord(s[A[-1]]) > ord(s[i])):
                indices.append(A[-1])
                A.pop()
        A.append(i)
        i += 1
    while A:
        indices.append(A.pop())
    return indices


def solve():
    s = input().strip()
    pos = int(input())
    n = len(s)

    l = 0
    r = n
    pos -= 1
    while (r-l > 1):
        m = (l+r)//2
        k = m
        if (((2*n-k+1)*k)//2 > pos):
            r = m
        else:
            l = m
    k = l

    # print(k+1)
    pos -= ((2*n-k+1)*k)//2
    # print(pos)

    # print(k)
    s = list(s)
    ignore = set(indices_to_be_removed_nex(s)[:k])

    cnt = -1
    i = 0
    while cnt < pos:
        if i not in ignore:
            cnt += 1
        i += 1
    ans = s[i-1]

    '''NOW pos is the index in s_{k} required'''

    ## needs to print without spaces ##
    print(ans, end='')


for _ in range(int(input())):
    solve()
