if __name__=='__main__':
    n=int(input())
    E=set(map(int,input().split()))
    m=int(input())
    F=set(map(int,input().split()))
    print(len((E.difference(F))))
