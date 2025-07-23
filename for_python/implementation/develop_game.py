import sys

n, m = map(int, sys.stdin.readline().split())
c, r, dir = map(int, sys.stdin.readline().split())
game_map = []
for i in range(n):
    game_map.append(list(map(int, sys.stdin.readline().split())))

# 북,동,남,서
dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]
count = 1

dir = (dir+3)%4
dir_change = 0

while True:
    nc = c+dc[dir]
    nr = r+dr[dir]
    if 0 <= nc < m and 0 <= nr < n and game_map[nr][nc] == 0:
        count += 1
        game_map[r][c] = 2
        c = nc
        r = nr
        dir_change = 0
    elif dir_change == 4:
        nc = c-dc[dir]
        nr = r-dr[dir]
        if 0 <= nc < m and 0 <= nr < n and game_map[nr][nc] != 1:
            c = nc
            r = nr
            dir_change = 0
        else :
            break
    else:
        dir_change += 1

    dir = (dir+3)%4

print(count)