
n= int(input())
order= input().split()

spot= [1, 1]
for idx in order:
    if idx=='R' and spot[0]+1< n+1:
        spot[0]= spot[1]+1
    elif idx=='L' and 1<= spot[0]-1:
        spot[0]= spot[1]-1
    elif idx=='U' and 1<= spot[1]-1:
        spot[0]= spot[0]-1
    elif idx=='D' and spot[1]+1< n+1:
        spot[1]= spot[0]+1
print(spot)