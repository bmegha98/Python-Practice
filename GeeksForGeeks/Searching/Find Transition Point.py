'''
You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently.
Transition point is a point where "0" ends and "1" begins.
'''
'''
 # Using built-in function
 
 def transitionPoint(arr, n):
    try :
        return arr.index(1)
    except : return None
'''
def transitionPoint(arr, n):
    ind = -1
    for i in range(0,n):
        if arr[i] == 1:
            ind = i
            break
    
    if ind == -1 : return None
    return ind
