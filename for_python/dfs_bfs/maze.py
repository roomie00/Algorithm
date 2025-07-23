import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

step = deque()
step.append((0,0))
maze[0][0] = 2

while step:
    x,y = step.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1:
                step.append((nx,ny))
                maze[nx][ny] = maze[x][y] + 1

print(maze[n-1][m-1]-1)