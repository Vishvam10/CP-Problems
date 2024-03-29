class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& arr) {
        
        int n = arr.size();
        vector<int> ans(n, 0);
        stack<pair<int, int>> st;

        st.push({arr[n - 1], n - 1});

        for(int i = n - 2; i >= 0; i--) {

            while(!st.empty() && arr[i] >= st.top().first) {
                st.pop();
            }
            if(!st.empty()) {
                ans[i] = st.top().second - i;
            }
            st.push({arr[i], i});           
        }

        return ans;

    }
};