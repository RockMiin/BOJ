def solution(n):
    dp=[]
    result=0
    for i in range(n):
        cnt=[]
        while(True):
            cnt.append(i%2)
            i=i//2
            if i==0:
                break;
        dp.append(sum(cnt))

    for i in range(n-1):
        if dp[i]==dp[n-1]:
            result+=1
    print(result)
    return result






n=9
print(solution(n))