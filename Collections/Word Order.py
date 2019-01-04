from collections import OrderedDict
if __name__=='__main__':
    N=int(input())
    counts=OrderedDict()
    for i in range(N):
        word=input()
        if word not in counts.keys():
            counts[word]=0
        counts[word]+=1
    print(len(counts))
    print(' '.join(str(ch) for ch in counts.values()))
