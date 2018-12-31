if __name__=='__main__':
    T=int(input())
    for i in range(T):
        EleA=int(input())
        A=list(map(int,input().split()))
        EleB=int(input())
        B=list(map(int,input().split()))
        f=0
        for ch in A:
            if ch not in B:
                f=1
                break
            
        if f==1:
            print('False')
        else:
            print('True')
