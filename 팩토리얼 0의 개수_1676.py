
n= int(input())
res= 1
cnt= 0
for i in range(n, 0, -1):
    res*=i
arr= list(str(res))
arr.reverse()
for i in arr:
    if i != '0':
        break;
    cnt+=1
print(cnt)