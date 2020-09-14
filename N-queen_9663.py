
def check(x):
    for i in range(x):
        if row[x]==row[i]:
            return False
        if abs(row[x]-row[i])==x-i:
            return False
    return True

def dfs(x):
    global count

    # 만약 x가 n에 도달한다면 count 값을 1추가
    if x==n:
        count+=1
    else: # 아니라면 더 탐색을 해야함
        for i in range(n):
            # 일단 x번째 row에 i컬럼 자리에 넣는다고 생각
            row[x]=i
            if check(x):

                dfs(x+1)

n=int(input())
count=0
row=[0]*n
dfs(0)
print(count)