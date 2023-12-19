from random import randint as limits
import sys

def pprint(*args, **kwargs): print(*args, **kwargs)

def get_point(lim=int(1e9)):
    x,y = limits(0,lim), limits(0, lim)
    if DEBUG: pprint(f"[INFO] Genereatd point ({x}, {y})",file=sys.stderr)
    return (x,y)

T = limits(1, 2000)
# T = 50
pprint(T)
DEBUG = "DEBUG" in sys.argv

def testcase():
    n = limits(1, int(1e5)); n=2
    pprint(n)
    
    points = [get_point() for i in range(n+1)]
    pprint(*points[0])
    
    for i in range(1,n+1): print(*points[i])
    
    player = input()
    assert player in ["First", "Second"]
    
    not_taken = set(range(1,n+1)) 
    
    am_I_first = player == "Second"
    
    total_distance = 0
    last_point = points[0]
    
    if am_I_first:
        for i in range(n):
            if (i%2 == 0):
                p = not_taken.pop() # random startegy by me
                pprint(p)
                
                curr = points[p]
                
                total_distance += (curr[0]-last_point[0])**2 + (curr[1]-last_point[1])**2
                
                last_point = points[p]
            else:
                k = int(input())
                not_taken.remove(k)
                
                curr = points[k]
                
                total_distance += (curr[0]-last_point[0])**2 + (curr[1]-last_point[1])**2

                last_point = points[k]
    else:
        for i in range(n):
            if (i%2 != 0):
                p = not_taken.pop() # random startegy by me
                pprint(p)
                
                curr = points[p]
                
                total_distance += (curr[0]-last_point[0])**2 + (curr[1]-last_point[1])**2
                
                last_point = points[p]
            else:
                k = int(input())
                not_taken.remove(k)
                
                curr = points[k]
                
                total_distance += (curr[0]-last_point[0])**2 + (curr[1]-last_point[1])**2

                last_point = points[k]

    if ((total_distance % 2 == 0) and  am_I_first) or (not am_I_first and (total_distance%2 == 1)):
        return False
    return True


for _ in range(T):
    res = testcase()
    pprint("\033[31m[INFO] Failed !!\033[0m" if not res else "\033[32m[Info] Passed\033[0m", file=sys.stderr)