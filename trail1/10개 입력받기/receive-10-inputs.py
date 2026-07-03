integers = list(map(int, input().split()))
arr = []
i = 0

while 1:
    if i >= 10:
        break
    if integers[i] == 0:
        break
    
    arr.append(integers[i])
    i += 1

avg = sum(arr) / len(arr)
print(sum(arr), end=" ")
print(round(avg, 1 ))