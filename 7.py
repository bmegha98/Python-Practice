if __name__ == '__main__':
    l=[]
    scores=[]
    Names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    #print(l)
    for i in range(len(l)):
        marks=l[i][1]
        scores.append(marks)
    #print(scores)
    minScore=min(scores)
    Rem=[i for i in scores if i!=minScore]
    SecMin=min(Rem)
    #print(SecMin)
    for i in range(len(l)):
        if l[i][1]==SecMin:
            Names.append(l[i][0])
    Names.sort()
    #print(Names)
    for ch in Names:
        print(ch)
