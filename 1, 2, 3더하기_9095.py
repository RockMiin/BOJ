
test_case= int(input())
for i in range(test_case):
    dp = [1, 2, 4]
    n=int(input())
    for i in range(3, n):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n-1])

