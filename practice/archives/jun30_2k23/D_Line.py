import sys
input = sys.stdin.readline


def solve(n, s):
    # ls = [i for i in range(n) if s[i] == "L"]
    su = 0
    # wrong:list[tuple[int,int]] = []
    wrong = []  # [(delta_achieved_by_flipping_it, wrong_index),...]
    for i in range(n):
        if s[i] == "L":
            if i < n//2:
                wrong.append(n-1 - 2*i)
            su += i
        else:
            if i >= n//2:
                wrong.append(2*i - n + 1)
            su += n - 1 - i
    wrong.sort(reverse=True)
    for k in range(len(wrong)):
        print(wrong[k] + su, end=" ")
        su += wrong[k]
    print(" ".join([str(su)] * (n - len(wrong))))


for _ in range(int(input())):
    n = int(input())
    s = input()
    solve(n, s)
