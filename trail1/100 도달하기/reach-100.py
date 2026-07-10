N = int(input())

arr = [1, N]

while 1:
    arr.append(arr[-1] + arr[-2])
    if arr[-1] + arr[-2] > 100:
        arr.append(arr[-1] + arr[-2])
        break
    

print(*arr)