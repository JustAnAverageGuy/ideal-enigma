# n, q = map(int, input().strip().split())

# # ORs = defaultdict(int)
# ORs = [0]*n
# inps = []
# for _ in range(q):
#     i, j, OR = map(int, input().strip().split())
#     ORs[i-1] |= OR
#     ORs[j-1] |= OR
#     i, j = min(i, j), max(i, j)
#     inps.append((i-1, j-1, OR))
# A = [0]*n
# # print(ORs)
# inps.sort()
# for b in range(31):
#     for qu in inps:
#         i, j, o = qu
#     # print(i,j,o)
#         if ((o >> b) & 1) == 0:
#             continue
#         elif (ORs[j] >> b) & 1 == 0:
#             A[i] |= (1 << b)
#         else:
#             A[j] |= (1 << b)
# print(*A)

get_bit = lambda x,b:  ((x >> b) & 1)

def solve_bits(A,G,b):
    n = len(A)
    for i in range(n):
        for it in G[i]:
            if not get_bit(it[1],b):
                A[i] &= (~(1 << b))
    for i in range(n):
        if get_bit(A[i],b):
            A[i] &= ~(1 << b)
        for it in G[i]:
            if (not get_bit(A[it[0]],b)) and get_bit(it[1],b):
                A[i] |= (1 << b)
                break



n, q = map(int, input().strip().split())
G = {i: [] for i in range(n)}
for _ in range(q):
    i, j, OR = map(int, input().strip().split())
    i -= 1
    j -= 1
    G[i].append((j, OR))
    G[j].append((i, OR))

pt = 31
A = [~(1 << pt)]*n
for i in range(pt):
    solve_bits(A,G,i)
print(*A)

