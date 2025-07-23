import sys

loc = sys.stdin.readline()
x, y = ord(loc[0])-ord('a'), int(loc[1])-1

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<8 and 0<=ny<8:
        count += 1

print(count)