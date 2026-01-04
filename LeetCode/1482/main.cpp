class Solution {
public:
    int minDays(vector<int>& arr, int m, int k) {
        int n = arr.size();
        if (1LL * m * k > n) {
            return -1;
        }

        int low = *min_element(arr.begin(), arr.end());
        int high = *max_element(arr.begin(), arr.end());
        int ans = -1;

        auto bouquets = [&](int day) {
            int cnt = 0, flowers = 0;
            for (int i = 0; i < n; ++i) {
                if (arr[i] <= day) {
                    flowers++;
                    if (flowers == k) {
                        cnt++;
                        flowers = 0;
                    }
                } else {
                    flowers = 0;
                }
            }
            return cnt;
        };

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int res = bouquets(mid);

            if (res >= m) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }
};
