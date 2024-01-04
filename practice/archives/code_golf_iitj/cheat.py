#!/bin/python3
import sys

if '-h' in sys.argv:
    print(f"Usage: {sys.argv[0]} code_file_name.py", file=sys.stderr)

s = '\n'
with open(sys.argv[1], 'r') as f: s += f.read()

ans = []

for c in s: ans.append('\t'*ord(c))
hehe = ' '.join(ans)

print(
f"""
s = ' '
for c in '{hehe}'.split(s): s+=chr(len(c))
exec(s)
"""
)
