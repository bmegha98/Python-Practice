class Record:
    '''
    Objective : To create a Record.
    '''
    def __init__(self, key, others):
        '''
        Objective        : To initialize an object of type Record.
        Input Parameters :
        self(Implicit Parameter)-> Object of type Record.
                             key-> Integer to represent key of record.
                          others-> String representing  information in record.
        Output           : None
        '''
        self.key=key
        self.others=others
    def __str__(self):
        '''
        Objective        : To return string representation of an object of type Record.
        Input Parameters :
        self(Implicit Parameter)-> Object of type Record
        Output           : String representation of given object.
        '''
        return 'KEY : ' + str(self.key)+'\tNON-KEY : ' + str(self.others)
