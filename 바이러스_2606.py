from collections import deque

def bfs(v):
    q=deque([v])
    while q:
        now=q.popleft()
        if not visited[now]:
            visited[now]=True
            for e in com[now]:
                if not visited[e]:
                    q.append(e)
    print(sum(visited)-1)

n= int(input())
m= int(input())
com=[[] for i in range(n+1)]

for i in range(m):
    x, y= map(int, input().split())
    com[x].append(y)
    com[y].append(x)
# print(com)
for i in com:
    i.sort()
# print(com)
visited=[False]*(n+1)
bfs(1)
