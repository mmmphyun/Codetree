arr = list(map(int, input().split()))
num = [0] * 9

for e in arr:
    if e == 0:
        break
    if e >= 10:
        num[(e // 10)-1] += 1

idx = 1
for e in num:
    print(f"{idx} - {e}")
    idx += 1