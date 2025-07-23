import sys

x = int(sys.stdin.readline())
result = [0] * (x+1)

for i in range(2, x+1):
    result[i] = result[i-1] + 1

    if i % 5 == 0:
        result[i] = min(result[i], result[i//5]+1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i//3]+1)
    if i % 2 == 0:
        result[i] = min(result[i], result[i//2]+1)

print(result[x])