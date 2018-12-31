if __name__=='__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N= int(input())
    for i in range(N):
        command=input().split()
        if command[0]=='pop':
            m=s.pop()
        elif command[0]=='remove':
            s.remove(int(command[1]))
        else:
            s.discard(int(command[1]))
    print(sum(s))
