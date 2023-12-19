# import logging

# FORMAT = '%(message)s'
# LEVEL = logging.DEBUG
# logging.basicConfig(format=FORMAT, level=LEVEL)

# log = logging.getLogger(__name__)

# def logger(fn):
#     from functools import wraps
#     import inspect
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         log = logging.getLogger(fn.__name__)
#         # log.info(f'   will run {fn.__name__}, with args={tuple(args)},kwargs={tuple(kwargs)}' )

#         out = fn(*args, **kwargs)

#         log.info(f'output from {fn.__name__}, with args={tuple(args)},kwargs={tuple(kwargs)}, output={out}' )
#         # Return the return value
#         return out
#     return wrapper



from itertools import permutations



A = list(map(int,input().strip().split()))


# @logger
def check(a,b,c):
    a,b,c = sorted([a,b,c])
    if a+b  > c: return "TRIANGLE"
    if a+b == c: return "SEGMENT"
    return "IMPOSSIBLE"



hmm = {check(p[0],p[1],p[2]) for p in permutations(A)}
if 'TRIANGLE' in hmm:print("TRIANGLE")
elif "SEGMENT" in hmm: print("SEGMENT")
else: print("IMPOSSIBLE")
