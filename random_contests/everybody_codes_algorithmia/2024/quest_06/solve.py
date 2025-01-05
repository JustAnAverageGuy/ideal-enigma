import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)

from api import get_input
def solve_part_1():
    inp1 =  get_input( part=1,
        day=6, 
        year=2024,
    )

    # inp1 = \
    # """RR:A,B,C
    # A:D,E
    # B:F,@
    # C:G,H
    # D:@
    # E:@
    # F:@
    # G:@
    # H:@"""

    from collections import defaultdict

    children = defaultdict(list)
    parent  = defaultdict(str)
    depth  = defaultdict(int)
    depth["RR"] = 0

    counter = 0
    leaves = []

    for i in inp1.splitlines():
        node, childs = i.strip().split(':')
        childs = childs.strip().split(',')
        # print(node, childs)
        for child in childs:
            curr = child
            if child == '@':
                counter += 1
                leaves.append(counter)
                curr = counter
            children[node].append(curr)
            parent[curr] = node

    # for n, c in children.items(): print(n, c)
    # print("----PARENTS-----")
    # for n, c in parent.items(): print(n, c)

    stk = [
        "RR"
    ]

    while stk:
        node = stk.pop()
        for c in children[node]:
            depth[c] = depth[node] + 1
            stk.append(c)

    # for i,j in depth.items(): print(" "*j,i, j)


    depth_counts = [depth[leaf] for leaf in leaves]


    from collections import Counter
    c = Counter(depth_counts)
    # print(depth_counts)
    # print(c)

    curleaf = 0
    for i,j in c.items():
        if j == 1:
            uniq_depth = i
            break
    # print(uniq_depth)
    curleaf = 0
    for l in leaves:
        if depth[l] == uniq_depth:
            curleaf = l
            # print(curleaf)
            break

    path = ['@']
    while curleaf:
        curleaf = parent[curleaf]
        path.append(curleaf)
    print(*path[::-1],sep="")

def solve_part_2():
    inp1 =  get_input( part=2,
        day=6, 
        year=2024,
    )

    # inp1 = \
    # """RR:A,B,C
    # A:D,E
    # B:F,@
    # C:G,H
    # D:@
    # E:@
    # F:@
    # G:@
    # H:@"""

    from collections import defaultdict

    children = defaultdict(list)
    parent  = defaultdict(str)
    depth  = defaultdict(int)
    depth["RR"] = 0

    counter = 0
    leaves = []

    for i in inp1.splitlines():
        node, childs = i.strip().split(':')
        childs = childs.strip().split(',')
        # print(node, childs)
        for child in childs:
            curr = child
            if child == '@':
                counter += 1
                leaves.append(counter)
                curr = counter
            children[node].append(curr)
            parent[curr] = node

    # for n, c in children.items(): print(n, c)
    # print("----PARENTS-----")
    # for n, c in parent.items(): print(n, c)

    stk = [
        "RR"
    ]

    while stk:
        node = stk.pop()
        for c in children[node]:
            depth[c] = depth[node] + 1
            stk.append(c)

    # for i,j in depth.items(): print(" "*j,i, j)


    depth_counts = [depth[leaf] for leaf in leaves]


    from collections import Counter
    c = Counter(depth_counts)
    # print(depth_counts)
    # print(c)

    curleaf = 0
    for i,j in c.items():
        if j == 1:
            uniq_depth = i
            break
    # print(uniq_depth)
    curleaf = 0
    for l in leaves:
        if depth[l] == uniq_depth:
            curleaf = l
            # print(curleaf)
            break

    path = ['@']
    while curleaf:
        curleaf = parent[curleaf]
        if curleaf:
            path.append(curleaf[0])
    print(*path[::-1],sep="")
def solve_part_3():
    inp1 =  get_input( part=3,
        day=6, 
        year=2024,
    )

    # inp1 = \
    # """RR:A,B,C
    # A:D,E
    # B:F,@
    # C:G,H
    # D:@
    # E:@
    # F:@
    # G:@
    # H:@"""

    from collections import defaultdict

    children = defaultdict(list)
    parent  = defaultdict(str)
    depth  = defaultdict(int)
    depth["RR"] = 0

    counter = 0
    leaves = []

    for i in inp1.splitlines():
        node, childs = i.strip().split(':')
        childs = childs.strip().split(',')
        # print(node, childs)
        if node in ("ANT", "BUG"): continue
        for child in childs:
            if child in ("ANT", "BUG"): continue
            curr = child
            if child == '@':
                counter += 1
                leaves.append(counter)
                curr = counter
            children[node].append(curr)
            parent[curr] = node

    # for n, c in children.items(): print(n, c)
    # print("----PARENTS-----")
    # for n, c in parent.items(): print(n, c)

    stk = [
        "RR"
    ]

    while stk:
        node = stk.pop()
        for c in children[node]:
            depth[c] = depth[node] + 1
            stk.append(c)

    # for i,j in depth.items(): print(" "*j,i, j)


    depth_counts = [depth[leaf] for leaf in leaves]


    from collections import Counter
    c = Counter(depth_counts)
    # print(depth_counts)
    # print(c)

    curleaf = 0
    for i,j in c.items():
        if j == 1:
            uniq_depth = i
            break
    # print(uniq_depth)
    curleaf = 0
    for l in leaves:
        if depth[l] == uniq_depth:
            curleaf = l
            # print(curleaf)
            break

    path = ['@']
    while curleaf:
        curleaf = parent[curleaf]
        if curleaf:
            path.append(curleaf[0])
    print(*path[::-1],sep="")

solve_part_1()
solve_part_2()
solve_part_3()
