if __name__=='__main__':
    N,M=map(int,input().split())
    mid=N//2 + 1
    for i in range(1,mid):
        pattern='.|.'*(2*i-1)
        pattern=pattern.center(M,'-')
        print(pattern)
    print('WELCOME'.center(M,'-'))
    for i in range(mid-1,0,-1):
        pattern='.|.'*(2*i-1)
        pattern=pattern.center(M,'-')
        print(pattern)
