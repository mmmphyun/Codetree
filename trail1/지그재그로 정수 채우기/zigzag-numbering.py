N, M = map(int, input().split())

# Please write your code here.

arr = [[0] * M for _ in range(N)]
num = 0

for c in range(M):
    if c % 2 == 0:
        for r in range(N):
            arr[r][c] = num
            num += 1
    else:
        for r in range(N - 1, -1, -1):
            arr[r][c] = num
            num += 1

for r in range(N):
    for c in range(M):
        print(arr[r][c], end = " ")
    print()