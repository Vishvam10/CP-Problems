class Solution {
public:
    int maximumGap(vector<int>& arr) {
        int n = arr.size();
        int mx = *std::max_element(arr.begin(), arr.end());
        int mn = *std::min_element(arr.begin(), arr.end());

        int inf = 1e9;

        if(n < 2) {
            return 0;
        }
        if(mn == mx) {
            return 0;
        }

        int range = mx - mn;
        int bucket_size = max(1, range / (n - 1));
        int n_buckets = (range / bucket_size) + 1;

        // [][0] is min bucket and [][1] is max bucket
        int buckets[n_buckets][2];

        for(int i = 0; i < n_buckets; i++) {
            buckets[i][0] = inf;
            buckets[i][1] = -inf;
        }

        for(int i = 0; i < n; i++) {
            // x = mn + (ind * bucket_size)
            int ind = (arr[i] - mn) / bucket_size;
            buckets[ind][0] = min(buckets[ind][0], arr[i]);
            buckets[ind][1] = max(buckets[ind][1], arr[i]);
        }

        int ans = 0, prev = buckets[0][1];

        for(int i = 0; i < n_buckets; i++) {
            if(buckets[i][0] == inf) {
                continue;
            }
            ans = max(ans, buckets[i][0] - prev);
            prev = buckets[i][1];
        }

        return ans;

    }
};