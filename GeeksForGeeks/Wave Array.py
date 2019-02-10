'''
Given a sorted array A of non-repeating integers without duplicates. Sort the array into a wave-like array and return it. In other words, 
arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        i=0
        while i<N-1:
            tmp=A[i]
            A[i]=A[i+1]
            A[i+1]=tmp
            i+=2
        print(*A)
