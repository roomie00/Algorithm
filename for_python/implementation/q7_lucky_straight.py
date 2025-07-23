import sys

n = sys.stdin.readline().strip()

group = len(n)//2

sum1 = 0
sum2 = 0
for i in range(group):
    sum1 += int(n[i])

for j in range(group, len(n)):
    sum2 += int(n[j])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")