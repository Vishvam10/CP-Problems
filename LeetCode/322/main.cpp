class Solution {
public:
    int mp[12 + 1][10000 + 1];

    int solve(vector<int> coins, int ind, int target) {
        if(ind == coins.size() || target <= 0) {
            if(target == 0) {
                return 0;
            } else {
                return INT_MAX - 1;
            }
        }

        if(mp[ind][target] != -1) {
            return mp[ind][target];
        }
        
        int res = -1;

        if(coins[ind] > target) {
            int notake = solve(coins, ind+1, target);
            res = notake;
            mp[ind][target] = res;
        } else {
            int take = 1 + solve(coins, ind, target-coins[ind]);
            int notake = solve(coins, ind+1, target);
            res = min(take, notake);
            mp[ind][target] = res;
        }

        return mp[ind][target];

    }

    int coinChange(vector<int>& coins, int amount) {
        
        memset(mp, -1, sizeof(mp));
        int ans = solve(coins, 0, amount);
        if(ans == INT_MAX - 1) {
            return -1;
        }
        return ans;


    }
};