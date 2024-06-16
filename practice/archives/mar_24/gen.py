def gen(s):
    a = deque(s)
    n = len(s)
    A = defaultdict(list)
    A[s[0]].append(s)
    for i in range(n-1):
        a.rotate(1)
        si = "".join(a)
        A[si[0]].append(si)
    return A
    
        
