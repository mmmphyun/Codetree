mask = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

mat = [list(map(int, input().split())) for _ in range(4)]

result = [
    [a * b for a, b in zip(row_a, row_b)]
    for row_a, row_b in zip(mat, mask)
]

print(sum(sum(row) for row in result))