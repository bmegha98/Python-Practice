/*
Given a row-wise sorted matrix of N x M element.The task is to find the row with maximum 1s.
For each testcase, print the row number which contains maximum 1s if present, else print "-1" (without quotes).
*/

#include<iostream>
using namespace std;
int main() {
	int n;
	cin>>n;
	while(n--)
	{
	    int row,col;
	    cin>>row>>col;
	    int arr[row][col];
	    int count=0,index=-1;
	    for(int i=0;i<row;i++)
	    {
	        int temp=0;
	        for(int j=0;j<col;j++)
	        {
	            cin>>arr[i][j];
	            if(arr[i][j]==1)
	                temp++;
	        }
	        if(temp>count)
	        {
	            count=temp;
	            index=i;
	        }
	        
	        
	    }
	    cout<<index<<endl;
	}
	return 0;
}
