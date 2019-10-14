'''
Given two sorted arrays A and B of n elements each,describe an algorithm to find median of the union of two arrays in O(log n) time.
'''
def getMedian(A,B,n):
    if n == 0 : return -1
    if n == 1 :
        return (A[0]+B[0])//2
    
    if n == 2 :
        return (max(A[0],B[0])+min(A[1],B[1]))//2
    
    m1 = median(A,n)
    m2 = median(B,n)
    
    if m1 == m2 :
        return m1
    elif m1 > m2:
        if n%2 == 0:
            return getMedian(A[:(n//2)+1] , B[(n//2)-1:] ,(n//2)+1)
        
        else :
            return getMedian(A[:(n//2)+1] , B[(n//2):] , (n//2)+1)
    
    else :
        if n%2 == 0 :
            return getMedian(A[(n//2)-1:] , B[:(n//2)+1] ,(n//2)+1)
        
        else :
            return getMedian(A[(n//2):] , B[:(n//2)+1] , (n//2)+1)
            

def median(S , l):
    if l%2 == 0 :
        return (S[l//2]+S[(l//2)-1])//2
    else:
        return S[l//2]
    
if __name__ == '__main__':
    A = [1,12,15,26,38]
    B = [2,13,17,30,45]
    m = getMedian(A,B,5)
    print(m)
