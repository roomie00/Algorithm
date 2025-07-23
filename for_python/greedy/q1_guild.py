import sys

n = int(sys.stdin.readline())
count_group = 0
count_person = 0
adventurers = list(map(int,sys.stdin.readline().split()))
adventurers.sort()

for adventurer in adventurers:
    count_person += 1
    if count_person >= adventurer:
        count_group += 1
        count_person = 0

print(count_group)


"""
참고사항

for adventurer in adventurers:
<- 아래와 같은 에러 발생
    Traceback (most recent call last):
  File "/Users/roomie/IT_Engineer/coding_test/for_python/greedy/q1_guild.py", line 23, in <module>
    for adventurer in adventurers:
TypeError: 'PriorityQueue' object is not iterable
"""