import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())

min_distance = [-1]*(n+1)
min_distance[x] = 0
connects = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    connects[start].append(end)

move = deque([x])

while move:
    now = move.popleft()
    for next in connects[now]:
        if min_distance[next] == -1:
            min_distance[next] = min_distance[now]+1
            move.append(next)

for i in range(1, n+1):
    if min_distance[i] == k:
        print(i)
    elif i == n:
        print(-1)

"""
Traceback (most recent call last):
  File "/Users/roomie/IT_Engineer/coding_test/for_python/dfs_bfs/q15_distance_city.py", line 14, in <module>
    move = deque(x)
           ^^^^^^^^
TypeError: 'int' object is not iterable
"""