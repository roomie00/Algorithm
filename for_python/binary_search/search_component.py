import sys


n = int(sys.stdin.readline())
components = list(map(int, sys.stdin.readline().strip().split()))
components.sort()

m = int(sys.stdin.readline())
wanted = list(map(int, sys.stdin.readline().strip().split()))


def search(com, start, end):
    mid = (start + end) // 2
    if components[mid] == com:
        return True

    if components[mid] > com and mid != start:
        return search(com, start, mid-1)
    elif components[mid] < com and mid != end:
        return search(com, mid+1, end)
    else:
        return False


for i in range(m):
    if search(wanted[i], 0, n-1):
        print("yes", end= " ")
    else:
        print("no", end= " ")