'''
Given an array of integers, and an integer  ‘K’ , find the count of pairs of elements in the array whose sum is equal to 'K'.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        num = list(map(int,input().split()))
        N , K = num[0],num[1]
        A = list(map(int,input().split()))
        count = 0
        for i in range(N-1):
            for j in range(i+1,N):
                if A[i]+A[j]== K :count+=1
            
        print(count)
                
