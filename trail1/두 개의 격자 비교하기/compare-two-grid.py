N, M = map(int, input().split())

arr_1 = [list(map(int, input().split())) for _ in range(N)]
arr_2 = [list(map(int, input().split())) for _ in range(N)]

arr_r = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        if arr_1[r][c] != arr_2[r][c]:
            arr_r[r][c] = 1

for r in range(N):
    for c in range(M):
        print(arr_r[r][c], end=" ")
    print()