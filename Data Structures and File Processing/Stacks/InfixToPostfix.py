from Stack_Class import Stack
def InfixToPostfix(infix):
    '''
    Objective : To convert infix notation to postfix notation.
    Input     : Expression in infix form.
    Output    : Expression in postfix form.
    '''
    #Approach : if character is operand,append it with result string otherwise push it onto stack.
    #           If its precedence is low or equal to top element of stack,append that element with final string and push operator.
    s=Stack()
    postfix=[]
    OpPriorities={
                    ')':0,
                    '+':1,
                    '-':1,
                    '*':2,
                    '/':2,
                    '^':3,
                    '(':4
                    }
    for c in infix:
        if c.isalnum()==True:
            postfix.append(c)
        elif s.isEmpty():
            s.Push(c)
        elif OpPriorities[c]>OpPriorities[s.Top()]:
            s.Push(c)
        else:
            while s.isEmpty()!=True and OpPriorities[c]<=OpPriorities[s.Top()]:
                if s.Top()!='(':
                    postfix.append(s.Pop())
                elif c==')':
                    while s.Top()!='(':
                        postfix.append(s.Pop())
                    s.Pop()
                    break
                else:
                    break
            if c!=')':
                s.Push(c)
    while s.isEmpty()!=True:
        postfix.append(s.Pop())

    return ''.join(postfix)
def main():
    print('************************************INFIX TO POSTFIX*********************************')
    infix=input('Enter expression in infix notation :  ')
    print('Expression in postfix Notation  -->',InfixToPostfix(infix))

if __name__=='__main__':
    main()
    
                        
