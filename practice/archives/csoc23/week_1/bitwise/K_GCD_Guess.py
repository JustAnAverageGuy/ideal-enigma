# def solve():
#     suffix = 0
#     for i in range(1,30):
#         a = (1 << i) - suffix
#         b = a + (1 << i)
#         print(f'? {a} {b}',flush=True)
#         g = int(input())
#         if g == (1 << (i - 1)):
#             suffix |= (1 << (i - 1))
#     print(f'! {suffix}',flush=True)

def solve():
    suffix = 0
    for i in range(0, 30):
        a = (1 << i) - suffix
        b = a + (1 << (i+1))
        print(f'? {a} {b}',flush=True)
        g = int(input())
        if g == (1 << (i + 1)):
            suffix += (1 << (i) )
    print(f'! {suffix}',flush=True)


for _ in range(int(input())):
    solve()
