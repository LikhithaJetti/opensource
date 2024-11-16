T=int(input())
for i in range(0,T):
    L=list(map(int,input().split( )))
    X=L[0]
    Y=L[1]
    print(X//10*Y)
