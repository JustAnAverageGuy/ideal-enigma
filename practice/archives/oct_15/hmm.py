# def prin(*args,**kwargs):
#     kwargs["flush"] = kwargs.get("flush",True)
#     print(*args,**kwargs)

# from random import randint
# import sys

# T_MAX = 1_000
# T_MAX = 50

# N_MAX = 1_000_000_000
# M_MAX = 1_000_000_000

# N_MAX = 100
# M_MAX = 100


# t = randint(1,T_MAX)
# prin(t)

# def testcase(i):
#     n = randint(1,N_MAX)
#     m = randint(1,M_MAX)
#     r,c = randint(1,n), randint(1,m)
    
#     prin(n, m)
    
#     prin(f'# case-{i}: {n=} {m=} {r=} {c=}',file=sys.stderr)
#     count = 0
#     try:
#         while True:
#             s = input().strip()
            
#             if s[0] == '?':
#                 if count >= 3: raise IndexError("query count exceeded")
#                 count += 1
                    
#                 a,b = map(int,s.split()[1:])
                
#                 if (1<=a<=n) and (1<=b<=m):
#                     prin(max(abs(a-r), abs(b-c)))
#                 else:
#                     raise ValueError("Illegeal query")
#             else:
#                 a,b = map(int,s.split()[1:])
#                 if (a,b) == (r,c):
#                     prin("OK!",file=sys.stderr)
#                     return 0

#                 else:
#                     raise AssertionError("Incorrect Answer")
#     except KeyboardInterrupt:
#         sys.exit(130)
#     except Exception as e:
#         prin("Fail!",e,file=sys.stderr)
#         # sys.exit(69)

        
    

# for i in range(t): testcase(i)        
    
    
import os 
import sys
print(os.environ)

print(sys.argv)