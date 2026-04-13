from random import randint, shuffle
import sys
import os



DEBUG = os.environ.get("DEBUG", "").lower() == 'true'
# DEBUG = True
def debug(*args,force=False):
    if DEBUG or force: print(*args, file=sys.stderr)


T = randint(1, 10)
print(T, flush=True)

debug(f'{T = }')

for _ in range(T):
    n = randint(2, 50)
    n = randint(2, 10)
    secret = [*range(1,n+1)]*2
    shuffle(secret)
    # secret = [*range(1,n+1)]*2 # DELETE THIS
    print(n, flush=True)
    debug(f'     n= {n}')
    debug( 'secret=',*secret)
    limit = 3*n+1
    for _ in range(limit):
        query = input().strip()
        if query[0] == '!':
            claim = list(map(int, query[1:].strip().split()))
            if claim != secret: debug("\x1b[31mFAILED\x1b[0m 1", force=True); sys.exit(1)
            debug("\x1b[32mOK\x1b[0m", force=True)
            break
        else:
            assert query[0] == '?'
            indices = list(map(int, query[1:].strip().split()))[1:]
            maxdup = 0
            seen = set()
            for j in indices:
                assert 1 <= j <= 2*n
                if secret[j-1] in seen:
                    maxdup = max(maxdup, secret[j])
                else:
                    seen.add(secret[j])
            print(maxdup, flush=True)
    else:
        debug("\x1b[31mFAILED\x1b[0m 2", force=True); sys.exit(2) 

