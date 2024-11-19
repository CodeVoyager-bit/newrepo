n=int(input())
d1={}
d2={}
for i in range(n):
    n,m=map(int,input().split())
    if n in d1:
        d1[n]+=m
    else:
        d1[n]=m  
    if n in d2:
        d2[m]+=n
    else:
        d2[m]=n 

print(d1)
print(d2)