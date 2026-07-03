N = int(input())
arr = []
is_passed = [0] * N
count = 0

for i in range(N):
    arr = list(map(int, input().split()))
    avg = sum(arr) / 4

    if avg >= 60:
        is_passed[i] = 1

for e in is_passed:
    if e == 1:
        count += 1
        print('pass')
    elif e == 0:
        print('fail')

print(count)