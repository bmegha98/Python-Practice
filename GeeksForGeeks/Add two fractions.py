'''
You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of 
(numx/denx).
'''
def GCD(A,B):
    if A==0:return B
    if B==0:return A
    if A==B:return A
    if A>B:return GCD(B,A%B)
    if A<B:return GCD(A,B%A)
    
def addFraction(num1, den1, num2, den2):
    num=num1*den2 + num2*den1
    den=den1*den2
    gcd=GCD(num,den)
    numx=num//gcd
    denx=den//gcd
    print(numx,'/',denx,sep='')
