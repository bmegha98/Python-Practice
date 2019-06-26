'''
Given a matrix of size N X N, where N is odd. The task is to find the maximum sum out of all the triangles formed in the matrix as shown below:
Matrix:
1 2 3
4 5 6
7 8 9

Upper Triangle:
1 2 3
   5

Left Triangle:
1
4 5
7

Lower Triangle:
   5
7 8 9

Right Triangle:
   3
5 6
   9

Sum of all triangles up, left , low and right are as 11, 17, 29, 23 respectively. Maximum of all these is 29.
'''

#include<iostream>
using namespace std;

int Upper(int A[][1000],int N)
{
    int sum = 0;
    for(int i =0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
           if(i <= j)
           sum+=A[i][j];
           if(i == int(N/2) && j == int(N/2))
               return sum;
           
        }
	 }
}

int Lower(int A[][1000],int N)
{
    int sum = 0;
    int mid = N/2;
    sum+=A[mid][mid];
    for(int i =mid+1;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
           if(i >= j)
           sum+=A[i][j];
        }
	 }
    return sum;
}

int Left(int A[][1000],int N)
{
    int sum = 0;
    int mid = N/2;
    sum+=A[mid][mid];
    for(int i =0;i<N;i++)
    {
        for(int j =0;j<mid;j++)
        {
            if(i>=j)
            sum+=A[i][j];
            
        }
        
    }
    return sum;
}

int Right(int A[][1000],int N)
{
    int sum=0;
    int mid = N/2;
    sum+=A[mid][mid];
    for(int i =0;i<N;i++)
    {
        for(int j = N-1;j>mid;j--)
        {
            if(i<=j)
            sum+=A[i][j];
        }
    }
    return sum;
}

int Maximum(int A[4])
{
    int max = A[0];
    for(int i=0;i<4;i++)
    {
        if(max<A[i])
        max = A[i];
    }
    return max;
}
int main()
 {
	int T;
	cin>>T;
	while(T--)
	{
	    int N;
	    cin>>N;
	    int A[N][1000],Sum[4];
	    for(int i=0;i<N;i++)
	    {
	    for(int j=0;j<N;j++)
	    cin>>A[i][j];
	    }
	    
	    Sum[0] = Upper(A,N);
	   
	    Sum[1] = Lower(A,N);
	    
	    Sum[2] = Left(A,N);
	    
	    Sum[3] = Right(A,N);
	    
	    
	    cout<<Maximum(Sum)<<endl;
	}
	return 0;
}
