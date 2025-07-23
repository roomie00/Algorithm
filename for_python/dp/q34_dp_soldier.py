import sys

n = int(input())
soldiers = list(map(int, input().split()))
dyn = [1] * n   # 병사의 수

for i in range(1,n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dyn[i] = max(dyn[i], dyn[j] + 1)

print(n-max(dyn))