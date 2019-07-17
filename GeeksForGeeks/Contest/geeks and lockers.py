'''
Geek's high school has N lockers. On a particular day, Geeks decides to play a game and open only those lockers that are multiple of M. 
Initially all lockers are closed. Lockers are numbered from 1 to N. Find the number of lockers that remain closed.

Input:
First line of input contains testcase T. For each testcase, there will be two lines of input:
First line contains N, the number of lockers.
Second line contains M. Geeks will open lockers that are multiple of M.

Output:
For each testcase, print the number of lockers that remain closed.

Constraints:
1 <= T <= 100
1 <= N <= 107
0 <= M <= N

Example:
Input:
2
10
2
12
3

Output:
5
8

Explanation:
For testcase 1:
N = 10
M = 2
We have 10 lockers and Geek opens lockers numbered 2,4,6,8,10. So, the lockers that remain closed are 1,3,5,7,9. Which are a total of 5 lockers.
'''
def ClosedCount(N , M):
  multiples = list(range(M , N+1, M))
  return N - len(multiples)
