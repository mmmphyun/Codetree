N = int(input())
arr = list(map(float, input().split()))

avg = sum(arr) / N
print(round(avg, 1))

if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')