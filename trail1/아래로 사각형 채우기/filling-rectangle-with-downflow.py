N = int(input())
num = 1

for r in range(N):
    for c in range(N):
        print(num, end=" ")
        num += N
    print()
    num += (1 - N**2)