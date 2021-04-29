from collections import deque

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1
    desc=[[0]* m for _ in range(n)]
    while q:
        x, y= q.popleft()

        cnt= 0
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            tx, ty= x+ dx, y+ dy
            if 0<= tx< n and 0<= ty< m:
                if adj[tx][ty]==0: cnt+=1 # 인접한 바다의 수
                elif not visited[tx][ty]:
                    q.append([tx, ty])
                    visited[tx][ty]= 1
            desc[x][y]= cnt

    for i in range(n):
        for j in range(m):
            adj[i][j]= max(0, adj[i][j]- desc[i][j])

n, m= map(int, input().split())
adj= []
res= 0
for i in range(n):
    adj.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if adj[i][j]:
            visited = [[0] * m for _ in range(n)]
            bfs([i, j])
            for k in range(n):
                for v in range(m):
                    if not visited[k][v] and adj[k][v]:
                        print(res); exit(0);
            res+=1
print(0)