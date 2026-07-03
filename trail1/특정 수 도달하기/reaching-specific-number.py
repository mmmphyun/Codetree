arr = list(map(int, input().split()))

sum = 0
i = 0
count = len(arr)

while 1:
    if count == 0:
        break
    count -= 1
    
    if arr[i] >= 250:
        arr.pop(i)
        break
    
    sum += arr[i]
    i += 1

avg = round((sum / i), 1)

print(sum, avg)