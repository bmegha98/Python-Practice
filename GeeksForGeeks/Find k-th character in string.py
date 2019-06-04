'''
Given a decimal number m. Convert it in binary string and apply n iterations, in each iteration 0 becomes 01 and 1 becomes 10. 
Find kth character in the string after nth iteration.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists of three integers m,k,n.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        inp = list(map(int,input().split()))
        m , k , n  = inp[0],inp[1],inp[2] 
        
        bin_m = bin(m)[2:]
        for i in range(n):
            bin_m = bin_m.replace('0','x')
            bin_m = bin_m.replace('1','10')
            bin_m = bin_m.replace('x','01')
        print(bin_m[k])
