arr = list(map(int, input().split()))

odd = sum(arr[1::2])
even = sum(arr[::2])

print(max(odd, even) - min(odd, even))