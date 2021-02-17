
n, m= map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(n)]
res= 0
for i in arr:
    if res < min(i): res= min(i)
    # res= max(res, min(i))
print(res)