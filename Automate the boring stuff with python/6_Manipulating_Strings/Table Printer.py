def printTable(table):
    
    colWidth = [max([len(ele) for ele in lst]) for lst in table]
    row , col =  len(table[0]) , len(table)

    # Transpose table
    table = list(zip(*table))

    for i in range(row) :
        for j in range(col):
            print(table[i][j].rjust(colWidth[j]),end = ' ')
        print()
            
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
