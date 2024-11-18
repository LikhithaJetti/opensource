def reverse_array(L):
    n=len(L)
    for i in range(0,n//2):
        temp=L[i]
        L[i]=L[n-i-1]
        L[n-i-1]=temp
    return L
n=int(input())
L=list(map(int,input().split()))
print(' '.join(map(str,reverse_array(L))))
