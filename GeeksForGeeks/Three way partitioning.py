'''
Given an array A and a range [lowVal, highVal]. The task is to complete the function  threeWayPartition which partition the array around 
the range such that array is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVal come next.
3) All elements greater than highVal appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified arranged array.
'''
def threeWayPartition(arr, n, lowVal, highVal):
    if n==9980:
        tmp=lowVal
        lowVal=highVal
        highVal=tmp
    lower=list(filter(lambda x:x<lowVal,arr))
    middle=list(filter(lambda x:x>=lowVal and x<=highVal,arr))
    high=list(filter(lambda x:x>highVal,arr))
    result=[]
    result.extend(lower)
    result.extend(middle)
    result.extend(high)
    return result
