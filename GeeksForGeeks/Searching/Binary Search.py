'''
Given a sorted array A[](0 based index) and a key "k"  you need to complete the function bin_search to  determine the position of the key 
if the key is present in the array. If the key is not  present then you have to return -1. The arguments left and right denotes the left 
most index  and right most index of the array A[]. There are multiple test cases. For each test case, this function will be called 
individually.
'''

def Binary(arr,low,high,k):
    m = (low+high)//2
    if low>high:return -1
    if arr[m]== k:return m
    elif arr[m]<k : return Binary(arr,m+1,high,k)
    else : return Binary(arr,low,m-1,k)
    
def bin_search(arr, left, high, key):
    return Binary(arr,left,len(arr)-1,key)
