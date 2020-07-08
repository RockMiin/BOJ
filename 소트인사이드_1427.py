data = list(map(int, input()))

for i in range(len(data) - 1):
    tmp = i
    for j in range(i + 1, len(data)):
        if data[tmp] < data[j]:
            tmp = j
    data[i], data[tmp] = data[tmp], data[i]
for i in range(len(data)):
    print(data[i], end="")

# array=input()
#
# for i in range(9,-1,-1):
#     for j in array:
#         if int(j)==i:
#             print(i, end='')
