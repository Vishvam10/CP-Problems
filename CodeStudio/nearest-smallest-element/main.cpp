vector<int> solve(vector<int> &arr) {
	int n = arr.size();
	int smallest = arr[0];
	vector<int> ans(n, -1);
	
	for(int i = 1; i < n; i++) {
		if(arr[i] > smallest) {
			ans[i] = smallest;
		} else {
			ans[i] = -1;    
			smallest = arr[i];
		}
	}
	return ans;
	
}
