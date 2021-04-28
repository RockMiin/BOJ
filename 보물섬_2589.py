from collections import deque

def bfs(v):
    visited= [[0]* m for _ in range(n)]
    visited[v[0]][v[1]]= 1

    q= deque([v])
    while q:
        x, y= q.popleft()

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tx, ty= x+ dx, y+ dy
            if 0<= tx< n and 0<= ty< m:
                if not visited[tx][ty] and adj[tx][ty]=='L':
                    q.append([tx, ty])
                    visited[tx][ty]= visited[x][y]+ 1
    res= 0
    for i in visited:
        res= max(res, max(i))

    return res

n, m= map(int, input().split())
adj= []
for i in range(n):
    adj.append(list(input()))

ans= 0
for i in range(n):
    for j in range(m):
        if adj[i][j]=='L':
            tmp= bfs([i, j])
            ans= max(ans, tmp)

print(ans-1)