N = int(input())

arr = [N * i for i in range(1, 11)]
cnt = 0

for i in range(10):
    print(arr[i], end=" ")
    if arr[i] % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
