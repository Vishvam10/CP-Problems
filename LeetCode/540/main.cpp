class Solution {
public:
    int singleNonDuplicate(vector<int>& arr) {
        int n = arr.size();
        int low = 0, high = n - 1;

        if(n == 1) {
            return arr[0];
        }

        // n will always be odd. so, at mid, left size and right
        // size will be even. We have pairs, so one element in at
        // odd index and the other at even index 

        // [1, 1, 2, 3, 3, 4, 4, 8, 8]

        while(low <= high) {
            int mid = low + (high - low) / 2;

            if(
                mid % 2 == 0 && arr[mid] == arr[mid + 1] ||
                mid % 2 == 1 && arr[mid] == arr[mid - 1]
            ) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }

        }

        return arr[low];
        
    }
};