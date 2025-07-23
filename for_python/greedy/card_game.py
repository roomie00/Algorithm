import sys

n,m = map(int, sys.stdin.readline().split())
numbers = []
result = 0

for i in range(n):
    numbers.append(sorted(list(map(int, sys.stdin.readline().split()))))
    result = max(result, numbers[i][0])

print(result)