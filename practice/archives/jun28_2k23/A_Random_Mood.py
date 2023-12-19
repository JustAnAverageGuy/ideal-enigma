n,p = map(float,input().strip().split())

# def pow(a,b):
#     b = int(b)
#     ans = 1
#     p = a
#     while b:
#         if b & 1:
#             ans *= p
#         p *= p
#         b >>= 1
#     return ans


print("%.10f"%(0.5 + 0.5* pow((1 - 2 * p), n)))