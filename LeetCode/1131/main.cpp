#define fastio ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)

class Solution {
  public:
    int maxAbsValExpr(vector<int> &arr1, vector<int> &arr2) {
        fastio;
        int t1, t2, t3, t4;
        int mx1 = INT_MIN, mx2 = INT_MIN, mx3 = INT_MIN, mx4 = INT_MIN;
        int mn1 = INT_MAX, mn2 = INT_MAX, mn3 = INT_MAX, mn4 = INT_MAX;

        for (int i = 0; i < arr1.size(); i++) {
            t1 = arr1[i] + arr2[i] + i;
            t2 = arr1[i] + arr2[i] - i;
            t3 = arr1[i] - arr2[i] + i;
            t4 = arr1[i] - arr2[i] - i;

            mx1 = max(mx1, t1);
            mx2 = max(mx2, t2);
            mx3 = max(mx3, t3);
            mx4 = max(mx4, t4);

            mn1 = min(mn1, t1);
            mn2 = min(mn2, t2);
            mn3 = min(mn3, t3);
            mn4 = min(mn4, t4);
        }


        return max(max(mx1 - mn1, mx2 - mn2), max(mx3 - mn3, mx4 - mn4));
    }
};