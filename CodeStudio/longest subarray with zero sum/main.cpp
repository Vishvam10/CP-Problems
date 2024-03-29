class Subarray
{
public:
    int maxLen(vector<int> arr)
    {

        int n = arr.size();
        int pref = 0;
        int ans = 0;
        unordered_map<int, int> mp;

        // we want to consider the first occurence of 0
        mp[0] = -1;

        // we don't even check the (i, j) pairs of prefix sum
        // we just have to see if 2 elements are equal
        // and record the maximum diff in their positions

        for (int i = 0; i < n; i++)
        {
            pref += arr[i];
            if (mp.find(pref) == mp.end())
            {
                mp[pref] = i;
            }
            else
            {
                ans = max(ans, i - mp[pref]);
            }
        }

        // 3 1 0 -4
        // 3 4 0 0

        return ans;
    }
};