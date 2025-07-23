import sys

n = int(input())
graph = []
student = []
teacher = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if (graph[i][j] == 'T'):
            teacher.append((i,j))
        elif (graph[i][j] == 'S'):
            student.append((i,j))

hurdle = []

def watch(x, y):
    for sx,sy in student:
        if(sx == x or sy == y):
            hurdle.append(())
