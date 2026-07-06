arr_1 = [list(map(int, input().split())) for _ in range(3)]
input() # buffer
arr_2 = [list(map(int, input().split())) for _ in range(3)]
arr_r = [[0] * 3 for _ in range(3)]

for r in range(3):
    for c in range(3):
        arr_r[r][c] = arr_1[r][c] * arr_2[r][c]

for r in range(3):
    for c in range(3):
        print(arr_r[r][c], end=" ")
    print()