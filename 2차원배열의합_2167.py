
n, m= map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
k=int(input())
for _ in range(k):
    answer=0
    i, j, x, y= map(int, input().split())
    for row in range(i-1, x):
        answer+=sum(arr[row][j-1:y])
    print(answer)
