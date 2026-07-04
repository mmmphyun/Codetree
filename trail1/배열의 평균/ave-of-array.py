mat = [
    list(map(int, input().split()))
    for _ in range(2)
]

avg = []

for row in mat:
    avg.append(sum(row)/4)
    print(f"{avg[-1]:.1f}", end=" ")
print()
for col in zip(*mat):
    avg.append(sum(col)/2)
    print(f"{avg[-1]:.1f}", end=" ")
print()
print(f"{sum(avg)/6:.1f}")