'''
Given a number N, find the value of below equation for the given number.
for M in range 1 to N : sigma(pow(M+1 , 2)-(3M + 1) + M)
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = (n*(n+1)*(2*n + 1))//6
        print(res)
