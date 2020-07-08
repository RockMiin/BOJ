# 시간초과
# n= int(input())
# data=[]
# for i in range(n):
#     data.append(input().split())
#
# for i in range(len(data)):
#     min=0
#     for j in range(0, len(data)):
#         if data[min][0]>data[j][0]:
#             min=j
#     print(data[min][0], data[min][1])
#     data.pop(min)

n= int(input())
data=[]
for i in range(n):
    input_data=input().split()
    data.append((int(input_data[0]), input_data[1]))

data= sorted(data, key=lambda x:x[0])

for i in data:
    print(i[0],i[1])