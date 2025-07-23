import sys

n,m = map(int,sys.stdin.readline().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def virus(x,y):
    for i in range(4):
        

