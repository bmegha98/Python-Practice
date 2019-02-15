'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element
is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if 
sum(A) > sum(B).
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        tmp=list(filter(lambda x : x<0,A))
        if len(tmp)==0:print(*A)
        else:
            lst=[]
            j=0
            for i in range(len(tmp)):
                l=[]
                while j < len(A):
                    if A[j]!=tmp[i]:
                        l.append(A[j])
                        j+=1
                    else:
                        i+=1
                        j+=1
                        break
                lst.append(l)
            if j<len(A):
                lst.append([A[ch] for ch in range(j,len(A))])
            Sum=-1
            tmp=[]
            for i in range(0,len(lst)):
                if Sum<=sum(lst[i]):
                    Sum=sum(lst[i])
                    tmp=lst[i]
        
            print(*tmp)
