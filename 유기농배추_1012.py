from collections import deque
test_case=int(input())

def bfs(x, y):
    q= deque()
    q.append((x, y))
    directions=[(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        x, y= q.popleft()
        for dx, dy in directions:
            nx, ny= x+dx, y+dy
            # print(x, y)
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append([nx, ny])


for i in range(test_case):
    answer=0
    m, n, k= map(int, input().split())
    arr= [[0] * m for _ in range(n)]
    visited= [[0] * m for _ in range(n)]
    for j in range(k):
        y, x=map(int, input().split())
        arr[x][y]=1 # x, y값 조심 거꾸로 해야 하는 것을 인지
    for s in range(n):
        for t in range(m):
            if arr[s][t] and not visited[s][t]:
                bfs(s, t); answer+=1
    print(answer)