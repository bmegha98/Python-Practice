if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    lMax=max(l)
    lRun=[i for i in l if i!=lMax]
    RunScore=max(lRun)
    print(RunScore)
