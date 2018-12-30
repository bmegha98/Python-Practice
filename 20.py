def minion_game(string):
    vowels=['A','E',"I",'O','U']
    Stuart_Score=0
    Kevin_Score=0
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
