'''
Given a matrix mat of n*n. The task is to find the minimum difference between two columns Cj and Ci such that i < j, i.e., 
we need to find minimum value of sum(Cj) – sum(Ci) such that column i comes before column j.
For every test case you need to print the minimum difference. Print "Not Possible" (without quotes), if difference cannot be calculated.
'''
/*
// In C++

#include<bits/stdc++.h>
using namespace std;
int main()
 {
	int T;
	cin>>T;
	while(T--)
	{
	    int N;
	    cin>>N;
	    int A[N][N];
	    int Sum[N],k =0;
	    for(int i=0;i<N;i++)
	    {
	        for(int j=0;j<N;j++)
	        cin>>A[i][j];
	    }
	    for(int col=0;col<N;col++)
	    {
	        int sum = 0;
	        for(int row =0;row<N;row++)
	        sum+=A[row][col];
	        
	        Sum[k] = sum;
	        k++;
	    }
	    if(k == 1)
	    cout<<"Not Possible"<<endl;
	    else
	    {
	    int max = INT_MAX,diff;
	    for(int i =0;i<k-1;k++)
	    {
	        for(int j = i+1;j<k;j++)
	        {
	        diff = Sum[j]-Sum[i];
	        max = diff < max ? diff : max ;
	        }
	    }
	    cout<<max<<endl;
	    }
	}
	return 0;
}
*/

# In Python
import sys
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = []
        for i in range(N):
            row = list(map(int,input().split()))
            A.append(row)
        #print(A)
        Sum = []
        for col in range(N):
            sum = 0
            for row in range(N):
                sum+=A[row][col]
            Sum.append(sum)
        #print(Sum)
        if len(Sum) == 1 : print('Not Possible')
        else :
            Max = sys.maxsize
            for i in range(len(Sum)-1):
                for j in range(i+1,len(Sum)):
                    diff = Sum[j]-Sum[i]
                    #print('diff',diff)
                    Max = min(Max,diff)
            print(Max)
