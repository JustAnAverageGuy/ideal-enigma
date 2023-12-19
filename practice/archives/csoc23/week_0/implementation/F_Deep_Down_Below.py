def solve():
    n = int(input())
    caves = [list(map(int,input().strip().split())) for _ in range(n)] # caves[i][0] = k_{i} = length_of_the_cave
    min_pows = []
    for cave in caves:
        min_pow = cave[-1] + 1
        for j in range(cave[0]-1,0,-1): min_pow = max(min_pow - 1 ,cave[j]+1)
        min_pows.append((min_pow,cave[0]))
    min_pows.sort(key=lambda x: (x[0],-x[1]))
    # print(min_pows)
    offset = 0
    current = min_pows[0][0]+min_pows[0][1]
    for i in min_pows[1:]:
        if current < i[0]:
            offset += (i[0]  - current)
            current = i[0] + i[1]
        else:
            current += i[1]
    print(offset + min_pows[0][0])
    

for _ in range(int(input())):
    solve()