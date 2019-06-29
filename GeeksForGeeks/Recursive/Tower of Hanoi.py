'''
The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to 
another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs 
movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.
Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different
sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.
'''
def TowerOfHanoi(n,from_rod,spare_rod,to_rod):
    if n == 1 :
        print('move disk 1 from',from_rod,'to',to_rod)
        return
    TowerOfHanoi(n-1,from_rod,to_rod,spare_rod)
    print('move disk',n,'from',from_rod,'to',to_rod)
    TowerOfHanoi(n-1,spare_rod,from_rod,to_rod)
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        TowerOfHanoi(N,'rod 1','rod 2','rod 3')
        print(2**N-1)
