#include <deque>

class Solution {
public:

    vector<int> maxSlidingWindow(vector<int>& arr, int k) {
        
        int n = arr.size(), left = 0, right = 0;
        deque<int> dq;
        vector<int> ans;

        while(right < n) {

            while(!dq.empty() && arr[dq.back()] < arr[right]) {
                dq.pop_back();
            }

            dq.emplace_back(right);

            // remove elements out of the window
            if(left > dq[0]) {
                dq.pop_front();
            }

            // if window size is reached
            if(right >= (k - 1)) {
                ans.emplace_back(arr[dq.front()]);
                left++;
            }

            right++;
        }
        return ans;

    }
};