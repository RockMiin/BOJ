
n, m = map(int, input().split())
a=list(map(int, input().split()))
sum=0; max=0

for i in range(n:):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum=a[i]+a[j]+a[k]
            if(max<sum and sum <= m):
                max=sum
print(max)
