integers = list(map(int, input().split()))
count = 0
sum = 0

for i in range(len(integers)):
    if integers[i] == 0:
        break
    
    if integers[i] % 2 == 0:
        count += 1
        sum += integers[i]

print(f'{count} {sum}')
