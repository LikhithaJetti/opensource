def fact(X):
    if X==0 or X==1:
        return 1
    else:
        return X*fact(X-1)
X=int(input())
print(fact(X))
