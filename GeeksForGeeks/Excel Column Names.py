def ColumnName(n):
    Str=['']*50
    i=0
    while n>0:
        rem=int(n%26)
        if rem!=0:
            Str[i]=chr((rem-1)+ord('A'))
            n=n//26
        else:
            Str[i]='Z'
            n=(n//26)-1
        i+=1
    string = Str[::-1] 
    print(''.join(string)) 
    
    
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        ColumnName(N)
