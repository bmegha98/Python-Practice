'''
You are given N number of books. Every ith book has Pi number of pages. 
You have to allocate books to M number of students. There can be many ways or permutations to do so. In each permutation one of the M
students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation
in which the maximum number of pages allocated to a student is minimum of those in all the other permutations, and print this minimum value.

Each book will be allocated to exactly one student. Each student has to be allocated atleast one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order 
'''
import sys,math
def Possible(arr ,n,m,curr_min):
    students = 1
    curr_sum = 0
    for i in range(n):
        if arr[i] > curr_min:
            return False
        if curr_sum+arr[i] > curr_min:
            students+=1
            curr_sum = arr[i]
            if students > m :
                return False
        else :
            curr_sum+=arr[i]
    return True
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int,input().split()))
        M = int(input())
        if N<M : print(-1)
        else :
            start = 0
            end = sum(P)
            res = sys.maxsize
            while start<=end :
                mid = math.floor((start+end)/2)
                if(Possible(P,N,M,mid)):
                    res = min(res,mid)
                    end = mid-1
                else :
                    start = mid+1
        
            print(res)
