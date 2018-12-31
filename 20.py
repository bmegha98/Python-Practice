def minion_game(string):
    vowels=['A','E',"I",'O','U']
    Stuart_Score=0
    Kevin_Score=0
    '''
    // TLB Error
    for i in range(0,len(string)):
        for j in range(i,len(string)):
            l=[]
            for k in range(i,j+1):
                l.append(string[k])
            r=''.join(l)
            if r[0] not in vowels:
                Stuart_Score+=1
            else:
                Kevin_Score+=1
    '''
    for i in range(len(string)):
        if string[i] not in vowels:
            Stuart_Score+=len(string)-i
        else:
            Kevin_Score+=len(string)-i
    
    if Stuart_Score>Kevin_Score:
        print('Stuart',Stuart_Score)
    elif Kevin_Score>Stuart_Score:
        print('Kevin',Kevin_Score)
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
