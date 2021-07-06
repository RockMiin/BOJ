
def solution(n, start, end, m, adj):
    res = []

    def dfs(v):
        if v== end: res.append(visited[v])

        for i in adj[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                dfs(i)

    visited= [0]* (n+1)
    dfs(start)
    if not res: print(-1); return
    print(min(res))

n= int(input())
start, end= map(int, input().split())
m= int(input())
adj= [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

solution(n, start, end, m, adj)