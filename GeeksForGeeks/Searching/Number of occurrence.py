'''
Given a sorted array A of size N and a number X, you need to find the number of occurrences of X in A.
For each testcase, print the count of the occurrences of X in the array, if count is zero then print -1.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        numbers = list(input().split())
        N , X = numbers[0] , numbers[1]
        number = list(input().split())
        count = number.count(X)
        if count:print(count)
        else:print(-1)
