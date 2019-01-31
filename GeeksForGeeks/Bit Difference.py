'''
You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        num=list(map(int,input().split()))
        a,b=num[0],num[1]
        xor=a^b
        tmp=bin(xor)[2:]
        print(tmp.count('1'))
