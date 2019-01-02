class Stack:
    '''
    Objective: To implement a stack class and perform stack operations.
    '''
    stack=[]                #Empty Stack
    def __init__(self):
        '''
        Objective: To initialize a stack.
        Input    : Object of class Stack
        Output   : None
        '''
        self.stack=[]
        
    def Push(self,ele):
        '''
        Objective : To push an element onto stack.
        Input     : Integer
        Output    : None
        '''
        #Approach : Make use of append() function.
        self.stack.append(ele)
    def isEmpty(self):
        '''
        Objective : To check whether stack is empty.
        Input     : Object of class Stack
        Output    : Boolean value ; True if stack is empty.
        '''
        if len(self.stack)==0:
            return True
    def Pop(self):
        '''
        Objective : To pop an element from stack.
        Input     : None
        Output    : Element popped out of stack.
        '''
        #Approach : Make use of pop() function.
        if self.isEmpty()!=True:
            return self.stack.pop()

    def Top(self):
        '''
        Objective : To return top element of stack.
        Input     : Object of class Stack
        Output    : Top element of stack.
        '''
        
        return self.stack[-1]
            
    def Display(self):
        '''
        Objective: To display stack.
        Input     : Object of class Stack
        Output    : None
        '''
        for ch in range(len(self.stack)-1,-1,-1):
            print(self.stack[ch])
            print('_____')
        
def main():
    '''
    Objective : To ask user for stack operation and perform that operation.
    '''
    s=Stack()
    loop=True
    print('*********************STACK OPERATIONS************************')
    print('1. PUSH \n2. POP  \n3. DISPLAY \n4. EXIT ')
    print('************************************************************')
    while loop==True:
        choice=int(input('Enter Your Choice (1/2/3/4) :'))
        if choice==1:
            s.Push(int(input('\nEnter Element to be pushed :')))
        elif choice==2:
            if s.Pop()!=None:
                print('\nElement popped ->',s.Pop())
            else:
                print('Stack Underflow!!')
        elif choice==3:
            print('\nStack is :')
            s.Display()
        elif choice==4:
            loop=False
        else:
            print('\nWrong Choice!!')
        
    
              
if __name__=='__main__':
    main()

        
        
