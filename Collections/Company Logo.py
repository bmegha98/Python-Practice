from collections import Counter
if __name__=='__main__':
    s=sorted(input())
    string=Counter(s)
    #print(string)
    for ch,count in string.most_common(3):
        print(ch,count)
