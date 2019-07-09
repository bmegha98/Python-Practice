def printTable(table):
    
    colWidth = [max([len(ele) for ele in lst]) for lst in table]
    '''
    # Alternative Method
    row , col =  len(table[0]) , len(table)

    # Transpose table
    table = list(zip(*table))
    
    for i in range(row) :
        for j in range(col):
            print(ttable[i][j].rjust(colWidth[j]),end = ' ')
        print()
    '''
    for col in range(len(table[0])):
        for row in range(len(table)):
            print(table[row][col].rjust(colWidth[row]), end = ' ')
        print()
            
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
