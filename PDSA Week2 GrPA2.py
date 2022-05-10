L=[2,4,7,8,9]
def findLargest(L):
    Lo, Hi = 0, len(L)
    left = L[0]
    #right = L[-1]
    
    while(Lo<Hi):
        mid = (Lo+Hi)//2
        if(left > L[mid]):
            Hi = mid 
        else:
            Lo = mid + 1
    print('Lo',Lo)
    return L[Hi -1]




print(findLargest(L))


"""
Lo 0
Hi 6
left 7
right 6
mid 3
L{mid} 4
Hi 3

-----
Lo 0
Hi 3
left 7
right 6
mid 1
L[mid] 8
Lo 2
------
Lo 2
Hi 3
mid 2
left 7
right 6
L[mid] 2
Hi 2
------
L[2-1] 8


"""









