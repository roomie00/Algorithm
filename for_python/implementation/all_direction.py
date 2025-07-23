import sys

n = int(sys.stdin.readline())
move = list(sys.stdin.readline().split())

r,c = 0,0
for dir in move:
    if dir == "R" and c + 1 < n:
        c+=1
    elif dir == "D" and r + 1 < n:
        r+=1
    elif dir == "L" and 0 <= c - 1:
        c-=1
    elif dir == "U" and 0 <= r - 1:
        r-=1

print(r+1, c+1)