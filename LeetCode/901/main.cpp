#include <bits/stdc++.h> 
#include <stack>

/*
	This is signature of helper function 'knows'.
	You should not implement it, or speculate about its implementation.

	bool knows(int A, int B); 
	Function 'knows(A, B)' will returns "true" if the person having
	id 'A' know the person having id 'B' in the party, "false" otherwise.
*/

int findCelebrity(int n) {
 	
	stack<int> st;
	
	for(int i = 0; i < n; i++) {
		st.push(i);
	}

	while(st.size() > 1) {
		int A = st.top();
		int B = st.top();
		st.pop();
		st.pop();
		if(knows(A, B)) {
			st.push(B);
		} else {
			st.push(A);
		}
	}


	if(st.empty()) {
		return -1;
	}

	int ans = st.top();

	for(int i = 0; i < n; i++) {
		if(i != ans && (knows(ans, i) || !knows(i, ans))) {
			return -1;
		}
	}

	return ans;

}


















