import sys

n = int(sys.stdin.readline())
result = [0]*(n+1)
result[1] = 1
result[2] = 3

if n >= 3:
    for i in range(3, n+1):
        result[i] = result[i-1] + result[i-2]*2

print(result[n])