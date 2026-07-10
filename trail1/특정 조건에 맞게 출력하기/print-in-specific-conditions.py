arr = list(map(int, input().split()))
idx = 0

while 1:
    if arr[idx] == 0:
        break
    if arr[idx] % 2 == 0:
        print(arr[idx] // 2, end=" ")
    else:
        print(arr[idx] + 3, end=" ")
    idx += 1