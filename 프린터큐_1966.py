
N=int(input())
answer=[]
document=[]
for i in range(N):
    num, idx= list(map(int, input().split()))
    document= list(map(int, input().split()))
    cnt=0
    while document!=[]:

        if document[0]==max(document):
            document.pop(0); cnt+=1
            if idx==0: answer.append(cnt); break;
            else: idx-=1
        else:
            document.append(document.pop(0))
            if idx==0: idx=len(document)-1
            else: idx-=1
for i in range(len(answer)):
    print(answer[i])