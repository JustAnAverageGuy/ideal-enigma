import sys
input = sys.stdin.readline


def mean(a,b,k):
    return (a*(k+1) + b*k)/(2*k+1)

def cmp(a, b, opt):
    if a == b:
        return abs(opt - a)
    if a > b:
        avg = (a+b)/2
        if 2*opt <= (a+b):
            return int(abs(avg - opt))
        else:
            if opt >= a:
                return int(abs(opt - a))
            else:
                l = 0
                r = int(1e8)
                while r - l > 1:
                    m = (l+r)//2
                    k = m
                    if ((k+1)*a + k*b - (2*k+1)*opt < 0):
                        r = m
                    else:
                        l = m
                k = l
                return min(int(abs(opt-avg)),int(abs(opt - mean(a,b,k))), int(abs(opt - mean(a,b,k+1))))
    # a < b
    else:
        avg = (a+b)/2
        if 2*opt > a + b:
            return int(abs(avg - opt))
        elif 2*opt == a+b: return 0
        else:
            if opt <= a:
                return int(abs(opt - a))
            else:
                l = 0
                r = int(1e8)
                while r - l > 1:
                    m = (l+r)//2
                    k = m
                    if ((k+1)*a + k*b - (2*k+1)*opt > 0):
                        r = m
                    else:
                        l = m
                k = l
                return min(int(abs(opt-avg)),int(abs(opt - mean(a,b,k))), int(abs(opt - mean(a,b,k+1))))
        


for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    optimal = list(map(int, input().strip().split()))
    print(*sorted([i for i in range(n)],key=lambda x: cmp(A[x],B[x],optimal[x])))
