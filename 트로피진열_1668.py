N = int(input())
arr = []
right = 1
left = 1

for i in range(N):
    arr.append(int(input()))

max_l = arr[0]
max_r = arr[N - 1]
for i in range(N):
    if max_l < arr[i]:
        left += 1
        max_l = arr[i]
    if max_r < arr[N - 1 - i]:
        right += 1
        max_r = arr[N - 1 - i]

print(left)
print(right)
