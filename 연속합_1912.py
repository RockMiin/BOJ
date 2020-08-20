n= int(input())
arr=list(map(int, input().split()))
dp=[0]*n
answer=-1001
for i in range(n):
    dp[i]= max(dp[i-1]+arr[i], arr[i])
    answer= max(answer, dp[i])
print(answer)