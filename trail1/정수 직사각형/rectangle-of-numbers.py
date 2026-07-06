N,M = map(int, input().split())

arr = [[0] * M for _ in range(N)]
num = 1

for r in range(N):
    for c in range(M):
        print(num, end=" ")
        num += 1
    print()