'''
Given an array of N elements and a integer K. Your task is to return the position of first occurence of K in the given array.
Note: Position of first element is considered as 1.
For each test case, print the index of first occurrence of given number K. Print -1 if the number is not found in array.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        numbers = list(map(int,input().split()))
        N , K = numbers[0] , numbers[1]
        array = list(map(int,input().split()))
        try:
            ind = array.index(K)
            print(ind+1)
        except : print(-1)
