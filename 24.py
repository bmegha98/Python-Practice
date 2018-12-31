if __name__=='__main__':
    n,m=input().split()
    arr=map(int,input().split())
    A=set(map(int,input().split()))
    B=set(map(int,input().split()))
    happiness=0
    for ch in arr:
        if ch in A:
            happiness+=1
        elif ch in B:
            happiness-=1
    print(happiness)
