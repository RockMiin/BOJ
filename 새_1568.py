
N=int(input())
k=0; cnt=0
while(N>0):
   k+=1
   if(k<N):
       N=N-k; cnt+=1
       continue
   elif(k>N):
       k=0
   else:
       cnt+=1; break;

print(cnt)