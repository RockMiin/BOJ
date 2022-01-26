import math

def solution(progresses, speeds):
    answer= []
    
    todo= [0]* len(progresses)
    for i in range(len(progresses)):
        todo[i]= math.ceil((100- progresses[i]) / speeds[i])
    
    now= 0
    while now < len(progresses):
        cnt= 1
        for i in range(now+1, len(progresses)):
            if todo[now] >= todo[i]:
                cnt+=1
            else: break;
        
        answer.append(cnt)
        now +=cnt
    
    return answer
    
"""
그냥 단순한 구현 문제였다.
각 작업별 필요한 일 수를 구한 다음 하나씩 탐색하면서 현재 값보다 큰 값이 나올때까지 탐색하면서 이동을 하는 느낌
math.ceil을 이용해 올림이 가능함 !
"""

