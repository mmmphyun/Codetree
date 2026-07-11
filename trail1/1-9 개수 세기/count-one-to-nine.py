N = int(input())
arr = [0] * 9

given_num = list(map(int, input().split()))

for e in given_num:
    arr[e-1] += 1

for e in arr:
    print(e)