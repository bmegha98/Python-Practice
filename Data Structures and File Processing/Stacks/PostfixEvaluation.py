from Stack_Class import Stack
def PostFixEvaluation(postfix):
    '''
    Objective : Evaluate postfix notation.
    Input     : Expression in postfix form
    Output    : Result after evaluation.
    '''
    #Approach : If character is operand,push it onto the stack otherwise pop top two elements and perform corresponding operation and push result onto stack.
    s=Stack()
    for c in postfix:
        if c.isdigit()==True:
            s.Push(c)
        else:
            op1=s.Pop()
            op2=s.Pop()
            res=eval(op2+c+op1)
            s.Push(str(res))
    return s.Pop()
def main():
    postfix=input('Enter postfix expression: ')
    print(PostFixEvaluation(postfix))
if __name__=='__main__':
    main()
            
        
