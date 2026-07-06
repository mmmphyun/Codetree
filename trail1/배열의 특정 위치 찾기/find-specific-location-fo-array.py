arr = list(map(int, input().split()))

print(sum(arr[1::2]), end=" ")
avg = (arr[2]+arr[5]+arr[8])/3
print(round(avg,1))