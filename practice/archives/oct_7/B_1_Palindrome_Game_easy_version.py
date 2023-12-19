# ⣿⣿⣯⠉⠄⠄⠄⠄⠄⠄⡄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⡟⠁⠄⠄⠄⠄⠄⢀⢀⠃⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⡇⠄⠄⣾⣳⠄⠄⢀⣄⣦⣶⣴⠂⢒⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⡄⠄⠈⠚⡆⠄⢸⣿⣿⣿⣯⠋⡏⠄⠄⢸⣿⣿⣿⠿⠛⠛⠿⣿⣿⣿⣿⣿
# ⣿⣿⠟⣂⣀⣀⣀⡀⠠⠻⣷⣎⡼⠞⠓⠦⣤⣛⣋⣭⣴⣾⣿⣿⣷⣌⠻⣿⣿⣿
# ⣿⠋⣼⣿⣿⣿⣿⣿⣷⣦⣍⣙⠻⠳⠄⠄⠈⠙⠿⢿⣿⣿⣿⣿⣿⡟⣰⣿⣿⣿
# ⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⣀⠄⠄⢀⣤⣤⣭⡛⠛⣩⣴⣿⣿⣿⣿
# ⣷⠸⠿⠛⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠷⠦⣹⣿⣿⣿⣿
# ⣿⣧⠄⠄⠄⢀⣴⣷⣶⣦⣬⣭⣉⣙⣛⠛⠿⠿⠿⠟⠁⡀⠄⠄⠄⢁⣿⣿⣿⣿
# ⣿⣿⡅⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣍⠲⣶⣤⣄⡀⠄⣴⣿⣿⣿⣿⣿
# ⣿⣿⣷⠄⣾⡏⢿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠄⠹⣷⡌⢿⣿⣿⣷⣦⡙⢿⣿⣿⣿
# ⣿⣿⣿⣷⡌⢷⡘⣿⣿⣿⣿⣿⣿⣧⣀⣀⡀⠄⠈⠹⡈⣿⣿⣿⣿⣿⣦⡙⣿⣿
# ⣿⣿⣿⣿⣿⣎⢷⡘⢿⣿⣿⣿⣿⣿⣿⣿⠃⠄⣼⣶⡇⣿⣿⣿⣿⣿⣿⠓⠜⣿
# ⣿⣿⣿⣿⣿⣿⣎⢻⣦⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⣿⣿⣿⣿⣿⣿⣄⡀⢸
# ⣿⣿⣿⣿⣿⡿⢃⢼⣿⣿⣷⣤⣍⣉⣙⣛⣛⣉⣥⡄⠄⢿⣿⣿⣿⣿⡿⠟⣥⣿
# ⣿⣿⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⢁⣷⣤⣍⣉⣉⣭⣴⣾⣿⣿

import sys;input=sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    zeroes = s.count("0")
    if zeroes == 0:
        print("DRAW")
        return
    if zeroes%2 == 1 and zeroes > 1:  print("ALICE");return
        
        
    print("BOB")
    return


for _ in range(int(input())): solve()