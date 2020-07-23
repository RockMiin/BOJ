
N=int(input())
cnt=1
stack=[]
result=[]

for i in range(1, N+1):
    data=int(input())
    while cnt<=data:
        stack.append(cnt)
        result.append("+")
        cnt+=1
    if stack[-1]==data:
        stack.pop()
        result.append("-")
    else:
        print("NO"); exit(0)
print('\n'.join(result))
