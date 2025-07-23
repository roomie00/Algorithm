import sys

n,m = map(int, sys.stdin.readline().split())
homes = []
chickens = []
for r in range(n):
    c = 0
    for i in list(map(int, sys.stdin.readline().split())):
        if i == 1:
            homes.append([r,c])
        elif i == 2:
            chickens.append([r,c])
        c += 1

distance = [[0] * len(chickens) for _ in range(len(homes))]
distance_sum = []

for j in range(len(chickens)):
    sum_dis = 0
    for i in range(len(homes)):
        distance[i][j] = abs(homes[i][0] - chickens[j][0]) + abs(homes[i][1]-chickens[j][1])
        sum_dis += distance[i][j]
    distance_sum.append([j, sum_dis])

result = 0
if len(chickens) <= m:
    for i in range(len(homes)):
        result += min(distance[i][j] for j in range(len(chickens)))
else:
    distance_sum.sort(key=lambda x: x[1])
    for i in range(len(homes)):
        result += min(distance[i][j[0]] for j in distance_sum[0:m])

print(result)