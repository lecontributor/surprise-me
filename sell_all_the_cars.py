t= int(input())
for _ in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    m=10**9+7
    l.sort()
    p=len(l)-1
    for i in range(len(l)):
        if (l[i]-p)<0:
            l[i]=0
        else:l[i]-=p
        p-=1
    print(sum(l)%m)
