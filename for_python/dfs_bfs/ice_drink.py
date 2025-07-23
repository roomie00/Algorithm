import sys

n,m = map(int, sys.stdin.readline().split())
case = []

for i in range(n):
    case.append(list(map(int, sys.stdin.readline().split())))
count = 0

def dfs(x,y):
    if x >= 0 and x < n and y >= 0 and y < m and case[x][y] == 0:
        case[x][y] = 1
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    else:
        return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)