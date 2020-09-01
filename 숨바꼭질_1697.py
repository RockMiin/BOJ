from collections import deque

n, k= map(int, input().split())
MAX= 100001
def bfs(v):
    q= deque([v])
    arr= [0]*MAX
    # q가 빌 떄까지 반복을 실행한다 이건 재귀 아니고 반복으로 끝냄
    while q:
        v= q.popleft()
        if v==k: return arr[v]
        for i in (v-1, v+1, 2*v):
            # MAX보다 작고 방문하지 않았다면
            if 0 <= i < MAX and not arr[i]:
                arr[i]=arr[v]+1
                q.append(i)
print(bfs(n))
