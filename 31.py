if __name__=='__main__':
    size=int(input())
    A=set(map(int,input().split()))
    N=int(input())
    for i in range(N):
        operation=input().split()
        other= set(map(int,input().split()))
        if operation[0]=='intersection_update':
            A.intersection_update(other)
        elif operation[0]=='update':
            A.update(other)
        elif operation[0]=='symmetric_difference_update':
            A.symmetric_difference_update(other)
        elif operation[0]=='difference_update':
            A.difference_update(other)
    print(sum(A))
