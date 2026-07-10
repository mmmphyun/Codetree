N = int(input())
arr = list(map(int, input().split()))

even = [e for e in arr if e % 2 == 0]

print(*even)