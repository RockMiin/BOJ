
"""
    크기가 양수라는 말은.. -> 개수가
    n, s가 주어짐.. 1<= n <= 20, 절댓값 s <= 100만
    1. n 크기가 작으니까.. combination?
    2. list의 크기는 1부터 n까지여야 함..! -> 그래서 n+1까지 범위를 골라줘야 함..
"""

from itertools import combinations

n, s= map(int ,input().split())
cnt= 0
num= list(map(int, input().split()))

for i in range(1, n+1):
    n_lists= list(combinations(num, i))
    # print(n_lists)
    for n_list in n_lists:
        if sum(n_list)== s and len(n_list) >0:
            cnt+=1
            # print(n_list)

print(cnt)
