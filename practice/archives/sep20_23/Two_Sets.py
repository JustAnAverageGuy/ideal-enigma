n = int(input())

def solve(n):
    if n % 4 in [1,2]:
        print("NO")
        return
    else:
        target = (n*n+n)//4
        l = 1
        r = 1
        while r <= n:
            s = ((r-l+1)*(r+l))//2
            if s == target:
                print("YES")
                print(r-l+1)
                print(*range(l,r+1))
                print(n - r + l -1)
                print(*range(1,l),*range(r+1,n+1))
                return
            if s > target:
                l += 1
                continue
            if s < target:
                r += 1
                continue
        print("NO")
        return
solve(n)