#include <stack>

class Solution {
public:

    int get_height(int r, int c, int m, vector<vector<char>>& mat) {
        int res = 0;
        for(int j = c; j < m; j++) {
            if(mat[r][j] == '0') {
                return res;
            }
            res += 1;
        }
        return res;
    }

    int maximalRectangle1D(vector<int> arr) {
        int n = arr.size();
        int lefts[n], rights[n];
        int ans = 0;
        stack<pair<int, int>> st;

        for(int i = 0; i < n; i++){
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

        for(int i = n - 1; i >= 0; i--){
            while(!st.empty() && arr[i] <= st.top().first) {
                st.pop();
            }
            if(st.empty()) {
                rights[i] = (n - 1);
            } else {
                rights[i] = st.top().second - 1;
            }
            st.push({arr[i], i});
        }

        for(int i = 0; i < n; i++) {
            ans = max(ans, arr[i] * (rights[i] - lefts[i] + 1));
        }

        return ans;

    }

    int maximalRectangle(vector<vector<char>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        int ans = 0;

        vector<vector<int>> arrs;
        vector<int> hs;

        for(int j = 0; j < m; j++) {
            hs.clear();
            for(int i = 0; i < n; i++) {
                int h = get_height(i, j, m, mat);
                hs.emplace_back(h);
            }
            arrs.emplace_back(hs);
        }

        for(auto& arr: arrs) {
            int res = maximalRectangle1D(arr);
            ans = max(ans, res);
        }
        
        return ans;
        
    }
};