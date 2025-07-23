import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
count_group = 0
adventurers = PriorityQueue(maxsize=n)

for i in list(map(int,sys.stdin.readline().split())) :
    adventurers.put((-i, i))

while not adventurers.empty():
    count_person = adventurers.get()[1]-1

    if adventurers.qsize() >= count_person:
        for _ in range(count_person):
            adventurers.get()
        count_group += 1
    else:
        break

print(count_group)