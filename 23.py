def SetDifference(M,N):
    l=[]
    l.extend(M.difference(N))
    l.extend(N.difference(M))
    l.sort()
    return l

def main():
    x=int(input())
    M=set(map(int,input().split()))
    y=int(input())
    N=set(map(int,input().split()))
    diff=SetDifference(M,N)
    for ch in diff:
        print(ch)

if __name__=='__main__':
    main()
