#include <stack>

class Solution {
public:
    int largestRectangleArea(vector<int>& arr) {
        int n = arr.size();
        stack<pair<int, int>> st;
        int lefts[n], rights[n];
        int ans = 0;

        for(int i=0; i<n; i++) {
            while(!st.empty() && arr[i] <= st.top().first) {
                st.pop();
            }
            if(st.empty()) {
                lefts[i] = 0;
            } else {
                lefts[i] = st.top().second + 1;
            }
            st.push({arr[i], i});
        }

        while(!st.empty()) {
            st.pop();
        }

        for(int i=n-1; i>=0; i--) {
            while(!st.empty() && arr[i] <= st.top().first) {
                st.pop();
            }
            if(st.empty()) {
                rights[i] = (n-1);
            } else {
                rights[i] = st.top().second - 1;
            }
            st.push({arr[i], i});
        }
       
        for(int i=0; i<n; i++) {
            ans = max(ans, arr[i] * (rights[i] - lefts[i] + 1));
        }

        return ans;

    }
};