for _ in range(int(input())):
    n = int(input())
    s = input()
    k = s.find('1')
    if k == -1:
        print(s)
        continue
    if n - k - 1 < 2:
        print(s)
        continue
    print('0'*k + '1' + '0'*(n - k - 1))