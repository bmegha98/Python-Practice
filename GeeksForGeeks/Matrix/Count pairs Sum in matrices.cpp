'''
Given two matrices mat1 and mat2 of size N x N of  elements. Given a value x. The problem is to count all pairs from both matrices whose 
sum is equal to x.

INPUT: The first line consists of an integer T i.e. the number of test cases. The first line of each test case contains Two Integer N , x
denoting the size of the square Matrix. Next 2*N lines contain N integers separated by space.
'''
#include<iostream>
#include <unordered_map> 
using namespace std;
int main()
 {
	int T;
	cin>>T;
	for(int i = 0;i<T;i++)
	{
	    int N,x;
	    cin>>N>>x;
	    int A[N][N],B[N][N];
	    unordered_map<int,int> m;
	    for(int i =0;i<N;i++)
	    {
	        for(int j=0;j<N;j++)
	            cin>>A[i][j];
	    }
	    for(int i =0;i<N;i++)
	    {
	        for(int j=0;j<N;j++)
	        {
	            cin>>B[i][j];
	            m[B[i][j]]+=1;
	        }
	    }
	    
	    int count =0;
	    for(int i=0;i<N;i++)
	    {
	        for(int j=0;j<N;j++)
	        {
	            int sum = x-A[i][j];
	            if(m[sum]>0)
	            count+= m[sum];
	        }
	    }
	    
	    cout<<count<<endl;
	    
	}
	return 0;
}
