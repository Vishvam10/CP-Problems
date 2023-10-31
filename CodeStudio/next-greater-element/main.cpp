#include <stack>;

vector<int> nextGreaterElement(vector<int>& arr, int n)
{
	vector<int> ans(n, -1);
	stack<int> st;

	st.push(arr[n-1]);

	for(int i=n-2; i>=0; i--)
	{
		if(arr[i] < st.top()) 
		{
			ans[i] = st.top();
			st.push(arr[i]);
		} else 
		{
			while(!st.empty() && arr[i] >= st.top()) 
			{
				st.pop();
			}
			ans[i] = st.empty() ? -1 : st.top();
			st.push(arr[i]);
		}
	}
	return ans;

}