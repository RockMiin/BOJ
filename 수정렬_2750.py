
# n= int(input())
# data=list(map(int, input().split()))
#
# for i in range(n-1):
#     tmp=i
#     for j in range(i+1,n):
#         if data[i]>data[j]:
#             tmp=j
#     data[i], data[tmp]= data[tmp],data[i]
# for i in data:
#     print(i)

n=int(input())
data=list(map(int, input().split()))


for i in range(n):
    min=i
    for j in range(i+1,n):
        if data[min]>data[j]:
            min=j
    data[i], data[min]= data[min], data[i]
for i in data:
    print(i)