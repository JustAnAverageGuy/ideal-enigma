import sys;input=sys.stdin.readline

def solve():
    s = input().strip()
    length_of_array = 0
    status = {True}
    length_of_definitely_sorted_prefix = 0
    for i in s:
        if i == '1':
            if True in status:
                status = {True}
                length_of_definitely_sorted_prefix = length_of_array
                continue
            # print("Cannot be sorted")
            return False
        if i == '0':
            if False in status :
                status = {False}
                continue
            # print("Cannot be unsorted")
            return False
        if i == '+':
            length_of_array += 1
            if length_of_array < 2: 
                status = {True}
                length_of_definitely_sorted_prefix = length_of_array
                continue
            if (True in status) and (False not in status):
                status = {False,True}
                continue
        if i == '-':
            length_of_array -= 1
            if length_of_array < 2: 
                status = {True}
                length_of_definitely_sorted_prefix = length_of_array
                continue            
            if length_of_array <= length_of_definitely_sorted_prefix:
                length_of_definitely_sorted_prefix = length_of_array
                status = {True}
                continue
            status = {True,False}

    return True
        
        

for _ in range(int(input())): print("YES" if solve() else "NO")