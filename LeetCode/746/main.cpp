
// =============================================================================
// Brute Force
// =============================================================================


class Solution {
public:

    int solve(vector<int>& arr, int ind) {
        // As we can start from 1 as well, so no need to check for that base case
        if (ind == 0 || ind == 1) {
            return arr[ind];
        }
        int first = solve(arr, ind - 1);
        int second = solve(arr, ind - 2);
        return arr[ind] + min(first, second);
    }

    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        // Top floor
        cost.emplace_back(0);
        return solve(cost, n);
    }
};

// =============================================================================
// Optimized
// =============================================================================

class Solution {
public:


    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        // Top floor. But we take a reference so not doing it this way
        // We would just need to return ans[n] in this case
        // cost.emplace_back(0);

        vector<int> ans(n, 0);

        ans[0] = cost[0];
        if(n >= 2) {
            ans[1] = cost[1];
        }

        for(int i = 2; i < n; ++i) {
            ans[i] = cost[i] + min(ans[i - 1], ans[i - 2]);
        }

        return min(ans[n - 1], ans[n - 2]);
    }
};