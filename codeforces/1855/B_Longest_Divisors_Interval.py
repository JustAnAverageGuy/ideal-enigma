# # Sieve of Eratosthenes
# # Code by David Eppstein, UC Irvine, 28 Feb 2002
# # http://code.activestate.com/recipes/117119/
# from itertools import takewhile
# def gen_primes():
#     """ Generate an infinite sequence of prime numbers.
#     """
#     # Maps composites to primes witnessing their compositeness.
#     # This is memory efficient, as the sieve is not "run forward"
#     # indefinitely, but only as long as required by the current
#     # number being tested.
#     #
#     D = {}

#     # The running integer that's checked for primeness
#     q = 2

#     while True:
#         if q not in D:
#             # q is a new prime.
#             # Yield it and mark its first multiple that isn't
#             # already marked in previous iterations
#             #
#             yield q
#             D[q * q] = [q]
#         else:
#             # q is composite. D[q] is the list of primes that
#             # divide it. Since we've reached q, we no longer
#             # need it in the map, but we'll mark the next
#             # multiples of its witnesses to prepare for larger
#             # numbers
#             #
#             for p in D[q]:
#                 D.setdefault(p + q, []).append(p)
#             del D[q]

#         q += 1

# p = [*takewhile(lambda x: x < 500,gen_primes())]
# p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
#      37, 41, 43, 47, 53, 59, 61, 67, 71, 73]


def solve():
    n = int(input())
    c = 0
    i = 1
    while True:
        if n % i == 0:
            c += 1
            i += 1
        else:
            break
    print(c)


for _ in range(int(input())):
    solve()
