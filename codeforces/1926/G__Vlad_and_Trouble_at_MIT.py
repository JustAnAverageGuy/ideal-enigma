import sys;input=sys.stdin.readline

from collections import defaultdict

class tree:
    def __init__(self) -> None:
        self.n = int(input())

        self.parents = [None, None, *map(int,input().strip().split())]
        self.preference = "*"+input()

        self.children = defaultdict(list)
        for i in range(2,self.n+1): self.children[self.parents[i]].append(i)
        print("-"*20, file=sys.stderr)
        print(self.children, file=sys.stderr)
    
    def dfs(self, root=1):

        count_walls_in_subtree = 0
        has_unblocked_noisy_children = False
        has_sleepy
        
        my_mood = self.preference[root]
        has_sleepy_kids = False
        has_party_kids = False

        if my_mood == "C":
            for child in self.children[root]:
                if self.preference[child] == "S": has_sleepy_kids = True
                if self.preference[child] == "P": has_party_kids = True
                if has_party_kids and has_sleepy_kids: break

        for child in self.children[root]:
            count_walls_in_subtree_of_child, has_unblocked_grand_children = self.dfs(child)
            count_walls_in_subtree += count_walls_in_subtree_of_child
            if my_mood == "P":
                if self.preference[child] == "S": count_walls_in_subtree += 1
            elif my_mood == "S":
                if self.preference[child] == "P" or has_unblocked_grand_children: count_walls_in_subtree += 1
            else:
                if has_sleepy_kids and  self.preference[child] == "P": count_walls_in_subtree += 1
        print(f'node:{root} walls in subtree = {count_walls_in_subtree} has unblocked children = {has_unblocked_noisy_children}' ,file=sys.stderr)
        return count_walls_in_subtree, (has_unblocked_noisy_children or my_mood == "P") and (not my_mood == "S") and not has_sleepy_kids






            

        


def solve():
    graph = tree()
    count, has_children = graph.dfs()
    print(count)

    

for _ in range(int(input())): solve()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀HELO⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
# ⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
# ⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
# ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
#
# G. Vlad and Trouble at MIT
# 1000, 256
#
# https://codeforces.com/contest/1926/problem/G
# Monday 19 February 2024 20:08:39 +0530
#
