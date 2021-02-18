
n, m= map(int, input().split())
x, y, d= map(int, input().split())
move= [[-1, 0], [0, 1], [1, 0], [0, -1]]
adj= [list(map(int, input().split())) for _ in range(n)]

visited=[[0] * m for _ in range(n)]
cnt= 0
res= 1
visited[x][y]= 1
while True:
    if d==0: d=3
    else: d-=1
    tx, ty= x+ move[d][0], y+ move[d][1]
    # print('now', x, y, d)
    if not visited[tx][ty] and adj[tx][ty]==0: # 방문하지 않고 육지라면 전진
        visited[tx][ty]= visited[x][y]+1
        cnt= 0
        res+=1
        x, y= tx, ty
        # print("go:", x, y)
        for i in visited:
            print(i)
        print()
    else: cnt+=1

    # 이동을 하지 않고 회전을 4번 했다면 back 아니면 정지
    if cnt==4:
        tx, ty = x -move[d][0], y- move[d][1]

        if adj[tx][ty]==0:
            cnt= 0
            visited[tx][ty]= visited[x][y]
            x, y= tx, ty

            # print('back', x, y)

        else:
            # print('end', x, y)
            break;

print(res)

# 예제 입력
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
#
# 5 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 1
# 1 1 1 0 1
# 1 0 0 0 1
# 1 1 1 1 1
#
# 5 5
# 1 2 0
# 1 1 1 1 1
# 1 1 0 1 1
# 1 0 0 0 1
# 1 1 0 1 1
# 1 1 1 1 1