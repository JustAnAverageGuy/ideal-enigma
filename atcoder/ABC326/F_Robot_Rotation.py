
n, x, y = map(int, input().strip().split())
A = list(map(int, input().strip().split()))


vertical = A[::2]
horizontal = A[1::2]

Sy = sum(vertical)
Sx = sum(horizontal)


def gen_subset_sums(A):
    n = len(A)
    sums = dict()

    for i in range((1 << (n))):
        s = 0
        j = 0
        t = i
        while t:
            if t & 1:
                s += A[n-1-j]
            j += 1
            t >>= 1
        if s not in sums:
            sums[s] = i
    return sums


def check(A, target):
    s = sum(A)
    if s < target or target < -s or (s-target) % 2:
        return False, None
    # aise elements chun ne hai such that unka sum k ho, and fir unko -axis ke along chlenge and baakiyon ko +axis ke along

    # ab meet in the middle krkr bruteforce

    k = (s-target)//2
    n = len(A)

    L = A[:n//2]
    R = A[n//2:]

    lsums = gen_subset_sums(L)
    rsums = gen_subset_sums(R)

    for s in lsums:
        if k-s in rsums:
            return True, (lsums[s] << len(R)) | (rsums[k-s])
    return False, None


# print(bin(X[1])[2:].zfill(len(horizontal)))
# print(bin(Y[1])[2:].zfill(len(  vertical)))


X = check(horizontal, x)
Y = check(vertical, y)

if not (X[0] and Y[0]):
    print("No")
    exit(0)


print("Yes")
dirn = 1  # 1 if facing along positve axis  else -1 ig

ly = len(vertical)
lx = len(horizontal)

for i in range(n):
    k = i//2
    if i & 1:
        # odd step hence horizontal movement
        sgn = 1 - 2 * ((X[1] >> (lx-1-k)) & 1)

        print("R" if sgn*dirn > 0 else "L", end='')

        dirn = sgn

    else:
        # vertical movement
        sgn = 1 - 2 * ((Y[1] >> (ly-1-k)) & 1)

        print("R" if sgn*dirn < 0 else "L", end='')

        dirn = sgn
