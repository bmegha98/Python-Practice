if __name__=='__main__':
    A=set(map(int,input().split()))
    n=int(input())
    f=0
    for i in range(n):
        B=set(map(int,input().split()))
        f1,f2=0,0
        for ch in B:
            if ch not in A:
                f1=1
                break
        #print('f1',f1)
        if f1!=1:
            for ch in A:
                if ch not in B:
                    f2+=1
        #print('f2',f2)
        if f2>1:
            f+=1
        #print('f',f)
    if f==n:
        print('True')
    else:
        print('False')
