N = int(input())
arr = [[0] * N for _ in range(N)]
num = 1

for c in range(N-1, -1, -1):
    if N % 2 == 0:
        if c % 2 == 0:
            for r in range(N):
                arr[r][c] = num
                num += 1
        else:
            for r in range(N-1, -1, -1):
                arr[r][c] = num
                num += 1
    else:
        if c % 2 == 0:
            for r in range(N-1, -1, -1):
                arr[r][c] = num
                num += 1
        else:
            for r in range(N):
                arr[r][c] = num
                num += 1

for r in range(N):
    for c in range(N):
        print(arr[r][c], end=" ")
    print()
