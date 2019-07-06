def multiply(s1,s2):
    n1,n2 = len(s1),len(s2)
    res = [0]*(n1+n2)
    if n1 == 0 or n2 == 0 : return '0'
    i_n1 , i_n2 = 0 , 0
    for i in range(n1-1,-1,-1):
        carry = 0
        num1 = int(s1[i])
        i_n2 = 0
        for j in range(n2-1,-1,-1):
            num2 = int(s2[j])
            Sum = num1*num2 + carry + res[i_n1 + i_n2]
            carry = Sum // 10
            res[i_n1 + i_n2] = Sum % 10

            i_n2+=1

        if carry > 0 :
            res[i_n1 + i_n2]+= carry

        i_n1+=1

    i = len(res)-1
    while i>=0 and res[i]== 0 :
        i -=1

    if(i == -1): return '0'

    s = ''
    while i>=0 :
        s+= str(res[i])
        i-=1

    return s
    
            
def stringmultiply(s1,s2):
    sign1 , sign2 = s1[0],s2[0]
    
    if s1[0] == '-' and s2[0]!='-':
        s1 = s1[1:]
    elif s2[0] == '-' and s1[0]!='-':
        s2 = s2[1:]
    elif s1[0] == '-' and s2[0] == '-':
        s1 = s1[1:]
        s2 = s2[1:]

    res = multiply(s1,s2)
        
    if (sign1 == '-' or sign2 == '-') and (sign1!='-' or sign2!='-') and res!='0' :
        print('-',end='')

    return res

if __name__ == '__main__':
    s1 = input('Enter first string ')
    s2 = input('Enter second string ')
    res = stringmultiply(s1,s2)
    print(res)
