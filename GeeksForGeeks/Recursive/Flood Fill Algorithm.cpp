/*
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all 
adjacent(excluding diagonally adjacent) same colored pixels with the given color K.
*/

#include<bits/stdc++.h>
using namespace std;

void FloodFill(int A[][100] , int x,int y,int old , int color , int N , int M)
{
    if(x<0 || y<0 || x>= N || y>=M)
        return;
    if(A[x][y]!=old)
        return;
    else
    {
        A[x][y] = color;
        FloodFill(A , x+1,y,old,color,N,M);
        FloodFill(A, x,y+1,old,color,N,M);
        FloodFill(A , x-1,y,old,color,N,M);
        FloodFill(A, x , y-1,old ,color,N,M);
    }
    
}
int main()
 {
	int T;
	cin>>T;
	while(T--)
	{
	    int N,M;
	    cin>>N>>M;
	    int A[100][100];
	    for(int i =0;i<N;i++)
	        for(int j=0;j<M;j++)
	            cin>>A[i][j];
	   int x,y,K;
	   cin>>x>>y>>K;
	   int original = A[x][y];
	   
	   FloodFill(A,x,y,original,K,N,M);
	   for(int i =0;i<N;i++)
	        for(int j=0;j<M;j++)
	            cout<<A[i][j]<<" ";
	  cout<<endl;
	}
	return 0;
}
