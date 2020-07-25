N=int(input())

for i in range(N):
    left=[]
    right=[]
    arr=input()
    for j in arr:
        if j == '<':
            if left!=[]:
                right.append(left.pop())
        elif j == '>':
            if right!=[]:
                left.append(right.pop())
        elif j == '-':
            if left!=[]:
                left.pop(-1)
        else: left.append(j)
    left.extend(reversed(right))
    print("".join(left))

