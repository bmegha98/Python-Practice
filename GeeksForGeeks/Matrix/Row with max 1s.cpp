'''
Given a boolean 2D array where each row is sorted. Find the row with the maximum number of 1s.
'''
#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	while(n--)
	{
	    int row,col;
	    cin>>row>>col;
	    int arr[row][col];
	    int count=0,index=0;
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
