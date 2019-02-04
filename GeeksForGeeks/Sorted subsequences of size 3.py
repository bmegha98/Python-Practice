'''
Given an array A of N integers, Your task is to complete the function find3Numbers which finds any 3 elements in it such that
A[i]< A[j] < A[k] and i < j < k. You need to return them as a vector, if no such element is present then return the empty vector of size 0.
'''
 def find3number(n, A):
    seq=[]
    for i in range(1,n-1):
        x=A[i]
        y=min(A[:i])
        if y<x:
            z=max(A[i+1:])
            if x<z:
                seq.append((y,x,z))
    return seq
