# coding: utf-8
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 1
        
        cou = cnt(M)
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        mi_cnt[k] = min(mi_cnt[k], cou)
     return mi_cnt
        
        
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 1
        
        cou = cnt(M)
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        mi_cnt[k] = min(mi_cnt[k], cou)
    return mi_cnt
    
brute(2,2)
brute(2,4)
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 1
        
        cou = cnt(M)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,4)
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,4)
brute(2,2)
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            print("haha")
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,2)
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1; print("haha")
        
        cou = cnt(M)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,2)
def cnt(M):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        print(cou)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,2)
def cnt(M,debug=True):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        print(cou)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_an
    s
def cnt(M,debug=True):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        print(cou)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,2)
def cnt(M,debug=True):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M.copy()]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M.copy())
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,2)
def cnt(M,debug=True):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            mi_ans[k] = [M[:]]
        elif cou == mi_cnt[k]:
            mi_ans[k].append(M[:])
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    return mi_cnt, mi_ans
    
brute(2,2)
brute(2,4)
brute(2,4)[0]
def cnt(M,debug=False):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c,debug=False,extra=False):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    if extra: mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M,debug)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            if extra: mi_ans[k] = [M[:]]
        elif cou == mi_cnt[k]:
            if extra: mi_ans[k].append(M[:])
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    if extra: return mi_cnt, mi_ans
    return mi_cnt
    
brute(2,4))
brute(2,4)
brute(2,8)
brute(2,6)
brute(4,6)
brute(4,4)
brute(4,4)
brute(4,6,True)
brute(4,4,)
a = brute(4,4)
for i in range(len(a)*len(a[0])):
    print(f'{i:2}', a[i])
    
a = brute(4,4)
for i in range(len(a)):
    print(f'{i:2}', a[i])
    
def cnt(M,debug=False):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c,debug=False,extra=False):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    if extra: mi_ans = [[] for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M,debug)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            if extra: mi_ans[k] = [M[:]]
        elif cou == mi_cnt[k] and False:
            if extra: mi_ans[k].append(M[:])
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    if extra: return mi_cnt, mi_ans
    return mi_cnt
    
brute(4,4,extra=True)
def cnt(M,debug=False):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c,debug=False,extra=False):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    if extra: mi_ans = [list() for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M,debug)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            if extra: mi_ans[k] = [M[:]]
        elif cou == mi_cnt[k] and False:
            if extra: mi_ans[k].append(M[:])
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    if extra: return mi_cnt, mi_ans
    return mi_cnt
    
brute(4,4,extra=True)
def cnt(M,debug=False):
    c = 0
    for i in M:
        c += sum(i)&1
    for j in range(len(M[0])):
        c += sum(i[j] for i in M)&1
    if debug: print(c, M)
    return c
    

def brute(r,c,debug=False,extra=False):
    M = [[0]*c for _ in range(r)]
    mi_cnt = [float('inf')]*(r*c+1)
    if extra: mi_ans = [None for _ in range(r*c+1)]
    for mask in range(1, 1<<(r*c)):
        k = mask.bit_count()
        for i in range(r*c):
            x,y = divmod(i,c)
            if (mask >> i )&1: M[x][y] = 1
        
        cou = cnt(M,debug)
        if cou < mi_cnt[k]:
            mi_cnt[k] = cou
            if extra: mi_ans[k] = str(M)
        elif cou == mi_cnt[k] and False:
            if extra: mi_ans[k].append(M[:])
        
        for i in range(r*c):
            x,y = divmod(i,c)
            M[x][y] = 0
        
    if extra: return mi_cnt, mi_ans
    return mi_cnt
    
brute(4,4,extra=True)
[[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
[[0, 1, 1, 0],
 [1, 0, 1, 0],
  [1, 1, 0, 0],
   [0, 0, 0, 0]]
