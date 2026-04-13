import sys


n = int(input())

if n == 1:
    print("1 1")
    sys.exit(0)

last_ans = None

def query(i: int, j: int) -> int:
    global last_ans
    i += 1
    j += 1
    # if i > j: i,j = j,i
    if i == j and last_ans is not None:
        return last_ans
    print(i, j, flush=True)
    # print(f'<{i} {j}>',file=sys.stderr)
    res = int(input())
    last_ans = res
    if res == 0:
        # print("OK",file=sys.stderr)
        sys.exit(0)
    return res

def nc2(n:int)->int:
    if n <= 1: return 0
    return  n*(n-1)//2

known = []
known_invcounts = 0

remaining = [*range(1,n+1)]

a = query(1, n-1)
b = query(1, n-1)

x = (a+b - nc2(n-1)) // 2
y = b - x

known_invcounts = x
known.append(remaining.pop(x))


# print(f'{x:2} {y:2}',known_invcounts,known, alll,file=sys.stderr)

for i in range(1, n-1):
    c = query(i+1, n-1)
    c -= known_invcounts
    x = (c + y - nc2(n-i-1))//2
    y = nc2(n-i-1) + x - y
    known.append(remaining.pop(x))
    known_invcounts += x
    # print(f'{x:2} {y:2}',known_invcounts,known, alll,file=sys.stderr)

known.append(remaining.pop())
# print(f'{x:2} {y:2}',known_invcounts,known, alll,file=sys.stderr)

# print("FIXING", file=sys.stderr)
arr = known
for i in range(1,n):
    j = arr.index(i, i-1)
    query(i-1, j)
    arr = arr[:i-1]+[*reversed(arr[i-1:j+1])]+arr[j+1:]
    # print(arr, file=sys.stderr)





# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# Inversion Sorting
# 1000, 512
#
# https://cses.fi/problemset/task/3140
# Friday 17 October 2025 14:20:13 +0530
#
