'''
Given an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix (mat[][]) the task to check if the configuration has a
solution or not. 
'''
#include <bits/stdc++.h> 
using namespace std;

bool NotInRow(int A[][9],int row)
{
  set<int> st;
  for(int i=0;i<9;i++)
    {
        if(st.find(A[row][i])!= st.end())
        return false;
        if(A[row][i]!=0)
        st.insert(A[row][i]);
    }
    return true;
}

bool NotInCol(int A[][9],int col)
{
  set<int> st;
  for(int i=0;i<9;i++)
    {
        if(st.find(A[i][col])!= st.end())
        return false;
        if(A[i][col]!=0)
        st.insert(A[i][col]);
    }
    return true;
}

bool NotInBox(int A[][9],int startrow,int startcol)
{
    set<int> st;
    for(int row=0;row<3;row++)
    {
        for(int col=0;col<3;col++)
        {
            int ch = A[row+startrow][col+startcol];
            if(st.find(ch)!=st.end())
            return false;
            
            if(ch!=0)
            st.insert(ch);
        }
    }
    return true;
}

bool isValid(int A[][9],int row,int col)
{
    return NotInRow(A,row) && NotInCol(A,col) && NotInBox(A,row-row%3,col-col%3);
}
bool isValidConfig(int A[][9],int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(!isValid(A,i,j))
            return false;
        }
    }
    return true;
}
int main()
 {
	int T;
	cin>>T;
	while(T--)
	{
	    int A[9][9];
	    for(int i=0;i<9;i++)
	    {
	        for(int j=0;j<9;j++)
	        cin>>A[i][j];
	    }
	    if(isValidConfig(A,9))
	    cout<<'1'<<endl;
	    else
	    cout<<'0'<<endl;
	}
	return 0;
}
