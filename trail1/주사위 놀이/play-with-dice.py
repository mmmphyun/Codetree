dice = [0] * 6
arr = list(map(int, input().split()))

for e in arr:
    dice[e-1] += 1

idx = 1
for e in dice:
    print(f"{idx} - {e}")
    idx += 1