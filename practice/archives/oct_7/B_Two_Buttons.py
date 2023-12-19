megic = b"X>D+Ca&#bbd2<S5Y+-YAAa8SYa%Ev{Itm~lARuIAW*}c*Y;$O7W^`X)D05|OW-K6KDLM)uARr(hARr)VW*}i8Jv|_0Ze(ma3LqdLARr(hARr(hAai+hE^~BbZ*_DocXDZTWhf$CZXziPARr(hARr(hARr(hb9r+vb97{Hb#yLfY;|*JC@BgcARr(hARr)RY;$Eg3LqdLARr(hARr(hAai+hE^~BbZ*_DocXDZTWhirWawuUbDGDGUARr(hARuyObairWAaiAGW(s3(b#yEsWo~3_AUz;&b98cLVQnZWEFf=UYGq?|C@B";from base64 import b85decode as mage;exec(mage(megic).decode())

def solve(n,m):
    if m <= n: return n - m
    k = 0
    t = n
    while t < m:
        t <<= 1
        k += 1
    if t == m: return k
    ans = k
    d = t - m
    for i in range(k,-1,-1):
        f = d // (1 << i)
        ans += f
        d %= (1<<i)
    return ans

cout << solve(*map(int,input().strip().split())) << endl;
"""
⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⡴⠶⠟⠛⠛⠛⠛⠻⠶⢦⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣠⣴⡟⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⢻⣦⣄⠄⠄⠄⠄⠄
⠄⠄⠄⣠⡾⠋⠈⣿⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣶⣿⠁⠙⢷⣄⠄⠄⠄
⠄⠄⣴⠏⠄⠄⠄⠸⣇⠉⠻⣦⣀⠄⠄⠄⠄⣀⣴⠟⠉⣸⠇⠄⠄⠄⠹⣦⠄⠄
⠄⣼⠏⠄⠄⠄⠄⠄⢻⡆⠄⠄⠙⠷⣦⣴⠾⠋⠄⠄⢰⡟⠄⠄⠄⠄⠄⠹⣧⠄
⢰⡏⠄⠄⠄⠄⠄⠄⠈⣷⠄⢀⣤⡾⠋⠙⢷⣤⡀⠄⣾⠁⠄⠄⠄⠄⠄⠄⢹⡆
⣿⠁⠄⠄⠄⠄⠄⠄⠄⣸⣷⠛⠁⠄⠄⠄⠄⠈⠛⣾⣇⠄⠄⠄⠄⠄⠄⠄⠄⣿
⣿⠄⠄⠄⠄⠄⣠⣴⠟⠉⢻⡄⠄ ... ⠄⣾⡟⠉⠻⣦⣄⠄⠄⠄⠄⠄⣿
⣿⡀⠄⢀⣴⠞⠋⠄⠄⠄⠈⣷⠄⠄⠄⠄⠄⠄⣾⠁⠄⠄⠄⠙⠳⣦⡀⠄⠄⣿
⠸⣧⠾⠿⠷⠶⠶⠶⠶⠶⠶⢾⣷⠶⠶⠶⠶⣾⡷⠶⠶⠶⠶⠶⠶⠾⠿⠷⣼⠇
⠄⢻⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⡄⠄⠄⢠⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⡟⠄
⠄⠄⠻⣆⠄⠄⠄⠄⠄⠄⠄⠄⠘⣷⠄⠄⣾⠃⠄⠄⠄⠄⠄⠄⠄⠄⣰⠟⠄⠄
⠄⠄⠄⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⢹⣇⣸⡏⠄⠄⠄⠄⠄⠄⠄⣠⡾⠋⠄⠄⠄
⠄⠄⠄⠄⠄⠙⠳⣦⣄⡀⠄⠄⠄⠄⢿⡿⠄⠄⠄⠄⢀⣠⣴⠞⠋⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠳⠶⣦⣤⣼⣧⣤⣴⠶⠞⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄
"""