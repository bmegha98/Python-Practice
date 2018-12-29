if __name__ == '__main__':
    s = input()
    f1,f2,f3,f4,f5=0,0,0,0,0
    for ch in s:
        if ch.isalnum()==True:
            f1+=1
        if ch.isalpha()==True:
            f2+=1
        if ch.isdigit()==True:
            f3+=1
        if ch.islower()==True:
            f4+=1
        if ch.isupper()==True:
            f5+=1  
    if f1>0:
        print('True')
    else:
        print('False') 
    if f2>0:
        print('True')
    else:
        print('False') 
    if f3>0:
        print('True')
    else:
        print('False')
    if f4>0:
        print('True')
    else:
        print('False')
    if f5>0:
        print('True')
    else:
        print('False')      
