import sys

n, m = map(int, sys.stdin.readline().split())
tteoks = list(map(int,sys.stdin.readline().split()))

for h in range(max(tteoks), 0, -1):
    result = 0
    for tteok in tteoks:
        if tteok - h > 0:
            result += tteok-h

    if result >= m:
        break

print(h)