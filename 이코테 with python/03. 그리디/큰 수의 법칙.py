
n, m, k= map(int, input().split())
arr= list(map(int, input().split()))
arr= sorted(arr, reverse=True)
res= 0
for i in range(m):
    if i%k==0 and not i==0: res+= arr[1]; continue
    res+=arr[0]
print(res)