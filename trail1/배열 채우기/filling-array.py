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



for e in arr[::-1]:
    print(e, end=" ")