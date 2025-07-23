import sys

n = int(sys.stdin.readline())
storage = list(map(int, sys.stdin.readline().split()))
result = [0] * (n+1)
result[1] = storage[0]
result[2] = storage[1]

for i in range(3,n+1):
    result[i] = storage[i-1]
    try:
        result[i] = max(result[i], result[i-2]+storage[i-1])
        result[i] = max(result[i], result[i-3]+storage[i-1])
    except IndexError:
        pass

print(max(result))