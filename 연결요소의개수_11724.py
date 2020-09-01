from collections import deque
n, m= map(int, input().split())
arr=[[] for i in range(n+1)]
answer=0
def bfs(v):
    q=deque([v])
    while q:
        k=q.popleft()
        if not visited[k]:
            visited[k]=True
            for e in arr[k]:
                if not visited[e]:
                    q.append(e)

for i in range(m):
    x, y= map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited=[[False] for _ in range(n+1)]
for i in range(1, n+1):
    bfs(i); answer+=1
print(answer)