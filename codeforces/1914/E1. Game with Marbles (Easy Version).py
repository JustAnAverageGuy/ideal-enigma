import sys

input = sys.stdin.readline


def game(A, B, player):
    # player 0 = Alice => wants to maximize score,
    # player 1 = Bob => wants to minimize score
    possible_scores = []
    tempA, tempB = A[::], B[::]
    if player == 0:
        for k in range(len(A)):
            if A[k] and B[k]:
                tempA[k] -= 1
                tempB[k] = 0
                possible_scores.append(game(tempA, tempB, 1))
                tempA[k] += 1
                tempB[k] = B[k]
        if not possible_scores:
            return sum(A) - sum(B)
        return max(possible_scores)
    else:
        for k in range(len(A)):
            if A[k] and B[k]:
                tempB[k] -= 1
                tempA[k] = 0
                possible_scores.append(game(tempA, tempB, 0))
                tempB[k] += 1
                tempA[k] = A[k]
        if not possible_scores:
            return sum(A) - sum(B)
        return min(possible_scores)


def solve():
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    print(game(A, B, 0))


for _ in range(int(input())):
    solve()
