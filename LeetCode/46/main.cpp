class Solution {
public:

    vector<vector<int>> ans;

    void solve(vector<int>& arr, vector<int>& path, vector<bool>& used) {

        if(path.size() == arr.size()) {
            ans.emplace_back(path);
            return;
        }

        for(int i = 0; i < arr.size(); i++) {
            
            if(!used[i]) {

                // set the state
                path.emplace_back(arr[i]);
                used[i] = true;

                // goto next state
                solve(arr, path, used);

                // reset the state
                path.pop_back();
                used[i] = false;

            }
        }

        return;

    }

    vector<vector<int>> permute(vector<int>& arr) {
        
        vector<int> path;
        vector<bool> used(arr.size(), false);

        solve(arr, path, used);

        return ans;

    }
};