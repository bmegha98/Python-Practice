'''
Given a positive number N. The task is to round N to nearest multiple of 10. Number can be so big and can contains 1000 of digits.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        rem = N%10
        if rem == 0:
            print(N)
        elif rem <=5 :
            print(N-rem)
        else:
            print(N+(10-rem))
        
