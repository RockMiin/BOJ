
def solution(s):
    answer=0
    cnt= dict()
    for i in s:
        try: cnt[i]+=1
        except: cnt[i]=1

    for key, value in cnt.items():
        if value%2==1:
            answer+=1
    return answer
s= 'aabbbccd'
print(solution(s))