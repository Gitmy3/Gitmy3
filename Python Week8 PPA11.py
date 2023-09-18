def insert(L, x):
    if len(L) >0:
        if x < L[0]:
            return [x] + L
        else:
            return [L[0]] + insert(L[1: ],x)
    else:
        return [x]
    pass
def isort(L):
    if len(L)==1:
        return L
    return insert(isort(L[ :-1]), L[-1])

L=[1,5,4,3,2]
print(isort(L))



