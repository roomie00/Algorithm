import sys

n,m = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins = list(map(int, sys.stdin.readline().split()))
coins.sort()
result = [0] * (m+1)

if m in coins:
    print(1)
elif coins[0] > m:
    print(-1)
else:
    for i in range(coins[0],m+1):
        for coin in coins:
            if result[i] == 0:
                result[i] = result[i-coin]+1
            elif result[i] % coin == 0:
                result[i] = min(result[i], result[i]//coin)
            else:
                result[i] = min(result[i], result[i-coin]+1)
    print(result[-1])


