import sys

n = int(sys.stdin.readline())
schedule = []
for i in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))
dyn = [0]*(n+1)
max_value = 0

for i in range(n-1,-1,-1):
    if (n-i) >= schedule[i][0]:
        dyn[i] = max(schedule[i][1] + dyn[i+schedule[i][0]], max_value)
        max_value = dyn[i]
    else:
        dyn[i] = max_value
print(max_value)