n = int(input())
k = 0
while True:
    if int(bin(k)[2:]) > n:
        break
    k += 1

print(k-1)