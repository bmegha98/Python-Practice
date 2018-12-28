if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        Comm=input()
        inp=Comm.split()
        if len(inp)==1:
            comm=inp[0]
        elif len(inp)==2:
            comm=inp[0]
            arg1=int(inp[1])
        elif len(inp)==3:
            comm=inp[0]
            arg1=int(inp[1])
            arg2=int(inp[2])
        if comm=='insert':
            l.insert(arg1,arg2)
        elif comm=='print':
            print(l)
        elif comm=='append':
            l.append(arg1)
        elif comm=='remove':
            l.remove(arg1)
        elif comm=='pop':
            l.pop(len(l)-1)
        elif comm=='sort':
            l.sort()
        elif comm=='reverse':
            l.reverse()
