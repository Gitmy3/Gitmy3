'''def insert(L, x):
    for i in range(len(L)):
        if L[i] > [x]:
            break

    sorted_L = L + x  
    sorted_L = L[ :i] + [x] + L[i: ]
    return sorted_L

print(sorted_L)'''



def insert(L, x):
    for i in range(len(L)):
        if L[i] >= x:
            L.insert(i, x)
            break
        else:
            L.append(x)
    return L




                   
