import sys

n,m,k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers, reverse=True)

iter_num = m//(k+1)
result = numbers[1]*iter_num + numbers[0]*(m-iter_num)
print(result)