#!/bin/python3
import sys
with open(sys.argv[1]) as f:
    s = f.read()
c = 0
for i in s:
    if i not in [' ', '\t', '\n', '\r']: c += 1
print(c,"non whitespace characters")
