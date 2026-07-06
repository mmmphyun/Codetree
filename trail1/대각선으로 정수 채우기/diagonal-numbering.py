n, m = map(int, input().split())

# Please write your code here.

arr = [[0] * m for _ in range(n)]
num = 1

for k in range(n + m - 1):
    for r in range(k + 1):
        c = k - r
        if 0 <= r < n and 0 <= c < m:
            arr[r][c] = num
            num += 1

for r in range(n):
    for c in range(m):
        print(arr[r][c], end=" ")
    print()