if __name__ == '__main__':

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    print('\n' . join(''.join([grid[j][i]for j in range(9)]) for i in range(6)))
    '''
    Alternative method : use zip()
    
    print('\n'.join([''.join(x) for x in list(zip(*grid))]))
    '''
