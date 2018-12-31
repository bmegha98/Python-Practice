if __name__=='__main__':
    n=int(input())
    E=set(map(int,input().split()))
    m=int(input())
    F=set(map(int,input().split()))
    l=[]
    l.extend(E.difference(F))
    l.extend(F.difference(E))
    l.extend(E.intersection(F))
    print(len(l))
