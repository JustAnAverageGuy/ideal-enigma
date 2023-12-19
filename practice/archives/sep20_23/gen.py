import random,sys
MAX_N = 10
# MAX_N = 30
N = random.randint(1, MAX_N)
print(N)
A = [str(N)]+[str(random.randint(1,1500)) for i in range(N)]
print(*A)
# print(N,DNA,file=sys.stderr)
with open("random_test.in","w") as f: f.write("\n".join(A))